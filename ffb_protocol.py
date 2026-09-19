"""Serial protocol for talking to an OpenFFBoard over USB-CDC.

Wire format is taken 1:1 from the OpenFFBoard-configurator (PyQt6) reference
implementation (serial_comms.py):
    get command:  "<cls>.<instance>.<cmd><typechar>;"      typechar '?' = value, '!' = info
    set command:  "<cls>.<instance>.<cmd>=<value>;"
    reply:        "[<cls>.<instance>.<cmd><typechar>|<data>]"
"""
import queue
import re
import threading
import time

import serial
import serial.tools.list_ports

BAUDRATE = 115200
OFFICIAL_VID_PID = {(0x1209, 0xFFB0)}

# This GUI is built for exactly one firmware version and does not support
# updating/flashing the board in any way - it only warns on mismatch.
EXPECTED_FW = "1.16.6"

REPLY_RE = re.compile(
    r"\[(\w+)\.(?:(\d+)\.)?(\w+)([?!=]?)(?:(\d+))?(?:\?(\d+))?\|(.+)\]", re.DOTALL
)

HANDSHAKE_TIMEOUT = 2.0
KEEPALIVE_INTERVAL = 1.5


class FFBProtocol:
    """Owns the serial port, the read thread and the callback registry.

    All parsing happens on a background thread; parsed replies are pushed
    into a thread-safe queue and must be drained on the GUI thread via
    pump() (e.g. from a Tkinter .after() loop) so widget updates always
    happen on the main thread.
    """

    def __init__(self, on_log, on_connection_changed, on_incompatible_fw=None):
        self.on_log = on_log
        self.on_connection_changed = on_connection_changed
        self.on_incompatible_fw = on_incompatible_fw

        self.ser = None
        self.read_thread = None
        self.running = False
        self.rx_buffer = ""
        self.rx_queue = queue.Queue()

        # cls -> list of listener dicts: {cmd, instance, typechar, callback, oneshot}
        self.listeners = {}
        self._lock = threading.Lock()

        self.connected = False
        self.fw_version = None
        self._got_handshake = False
        self._keepalive_pending = False
        self._last_keepalive_ok = True

    # ------------------------------------------------------------------ ports
    @staticmethod
    def list_ports():
        return list(serial.tools.list_ports.comports())

    @classmethod
    def find_auto_port(cls):
        """Return a device path if exactly one official FFBoard device is present."""
        matches = [
            p for p in cls.list_ports() if (p.vid, p.pid) in OFFICIAL_VID_PID
        ]
        return matches[0].device if len(matches) == 1 else None

    @classmethod
    def is_official(cls, port_info):
        return (port_info.vid, port_info.pid) in OFFICIAL_VID_PID

    # ------------------------------------------------------------- connection
    def connect(self, portname):
        if self.connected:
            return True
        try:
            self.ser = serial.Serial(portname, BAUDRATE, timeout=0.05)
        except Exception as exc:
            self.on_log(f"Can not open port: {exc}")
            return False

        try:
            self.ser.dtr = True
        except Exception:
            pass

        self.running = True
        self.rx_buffer = ""
        self._got_handshake = False
        self.listeners.clear()
        self.read_thread = threading.Thread(target=self._read_loop, daemon=True)
        self.read_thread.start()

        self.connected = True
        self.on_log("Connecting...")
        self.on_connection_changed(True)

        self.request_once("main", "id", self._handshake_cb, instance=0)
        self.request_once("sys", "swver", self._version_cb, instance=0)
        threading.Timer(HANDSHAKE_TIMEOUT, self._check_handshake).start()
        return True

    def disconnect(self, reason=None):
        if reason:
            self.on_log(reason)
        was_connected = self.connected
        self.running = False
        self.connected = False
        if self.ser is not None:
            try:
                self.ser.close()
            except Exception:
                pass
        self.ser = None

        # Drop anything still in flight so no callback can later touch a
        # widget that the GUI is about to destroy.
        with self._lock:
            self.listeners.clear()
        while True:
            try:
                self.rx_queue.get_nowait()
            except queue.Empty:
                break

        if was_connected:
            self.on_log("Reset port")
            self.on_connection_changed(False)

    def _handshake_cb(self, _reply):
        self._got_handshake = True

    def _check_handshake(self):
        if self.connected and not self._got_handshake:
            self.disconnect("Can't detect board")

    def _version_cb(self, reply):
        ver = reply.strip()
        self.fw_version = ver
        self.on_log(f"FW v{ver}")
        if ver != EXPECTED_FW and self.on_incompatible_fw:
            self.on_incompatible_fw(ver, EXPECTED_FW)

    # ---------------------------------------------------------------- keepalive
    def keepalive_tick(self):
        """Call periodically (e.g. every KEEPALIVE_INTERVAL) from the GUI loop."""
        if not self.connected:
            return
        if self._keepalive_pending:
            self._keepalive_pending = False
            self.disconnect("Timeout. Please reconnect")
            return
        self._keepalive_pending = True
        self.request_once("main", "id", self._keepalive_cb, instance=0)

    def _keepalive_cb(self, _reply):
        self._keepalive_pending = False

    # ------------------------------------------------------------------- I/O
    def _read_loop(self):
        while self.running:
            try:
                data = self.ser.read(512)
            except Exception as exc:
                self.rx_queue.put(("__error__", str(exc)))
                return
            if data:
                self.rx_buffer += data.decode("utf-8", errors="ignore")
                self._extract_replies()

    def _extract_replies(self):
        while True:
            start = self.rx_buffer.find("[")
            end = self.rx_buffer.find("]")
            if start == -1 or end == -1 or end < start:
                break
            chunk = self.rx_buffer[start : end + 1]
            match = REPLY_RE.match(chunk)
            self.rx_buffer = self.rx_buffer[end + 1 :]
            if match:
                self.rx_queue.put(("__reply__", match.groups()))

    def pump(self):
        """Drain parsed replies and dispatch callbacks. Call from the GUI thread."""
        while True:
            try:
                kind, payload = self.rx_queue.get_nowait()
            except queue.Empty:
                break
            if kind == "__error__":
                self.disconnect(f"Serial error: {payload}")
                break
            else:
                self._dispatch(payload)

    def _dispatch(self, groups):
        cls, instance_s, cmd, typechar, _val1, _val2, reply = groups
        instance = int(instance_s) if instance_s else 0
        typechar = typechar or ""

        # Addressed (GETADR/SETADR) replies carry the channel address in one
        # of two places depending on echo style: a plain get-style echo
        # ("cmd?<adr>") puts it right after the typechar (_val1); a
        # set-style echo ("cmd=<val>?<adr>") puts the value there instead
        # and the address after the second "?" (_val2).
        if typechar == "?" and _val1 is not None:
            adr = int(_val1)
        elif typechar == "=" and _val2 is not None:
            adr = int(_val2)
        else:
            adr = None

        with self._lock:
            entries = list(self.listeners.get(cls, []))

        fired_oneshot_ids = set()
        for entry in entries:
            if entry["cmd"] != cmd or entry["instance"] != instance:
                continue
            if entry["typechar"] is not None and entry["typechar"] != typechar:
                continue
            if entry["adr"] is not None and entry["adr"] != adr:
                continue
            try:
                entry["callback"](reply)
            except Exception as exc:
                self.on_log(f"Callback error ({cls}.{instance}.{cmd}): {exc}")
            if entry["oneshot"]:
                fired_oneshot_ids.add(id(entry))

        if fired_oneshot_ids:
            with self._lock:
                if cls in self.listeners:
                    self.listeners[cls] = [
                        e for e in self.listeners[cls] if id(e) not in fired_oneshot_ids
                    ]

    def send_raw(self, text):
        if self.ser is not None and self.ser.is_open:
            try:
                self.ser.write(text.encode("utf-8"))
            except Exception as exc:
                self.on_log(f"Write error: {exc}")

    def send_get(self, cls, cmd, instance=0, typechar="?", adr=None):
        adr_part = "" if adr is None else str(adr)
        self.send_raw(f"{cls}.{instance}.{cmd}{typechar}{adr_part};")

    def set_value(self, cls, cmd, value, instance=0, adr=None):
        adr_part = "" if adr is None else f"?{adr}"
        self.send_raw(f"{cls}.{instance}.{cmd}={value}{adr_part};")

    def register(self, cls, cmd, callback, instance=0, typechar="?", adr=None):
        """Persistent listener: stays active until removed via unregister()."""
        entry = {
            "cmd": cmd,
            "instance": instance,
            "typechar": typechar,
            "adr": adr,
            "callback": callback,
            "oneshot": False,
        }
        with self._lock:
            self.listeners.setdefault(cls, []).append(entry)
        return entry

    def unregister(self, cls, entry):
        with self._lock:
            if cls in self.listeners and entry in self.listeners[cls]:
                self.listeners[cls].remove(entry)

    def request_once(self, cls, cmd, callback, instance=0, typechar="?", adr=None):
        """Send a get request and fire callback once when the matching reply arrives."""
        entry = {
            "cmd": cmd,
            "instance": instance,
            "typechar": typechar,
            "adr": adr,
            "callback": callback,
            "oneshot": True,
        }
        with self._lock:
            self.listeners.setdefault(cls, []).append(entry)
        self.send_get(cls, cmd, instance, typechar, adr=adr)
