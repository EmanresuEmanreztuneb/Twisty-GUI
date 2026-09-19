"""Optional HID side-channel for smooth axis/analog animation.

The FFBoard is a composite USB device (CDC + HID): the same physical board
also exposes a standard joystick HID interface (used by games), which pushes
input reports autonomously whenever a value changes - unlike the CDC text
protocol in ffb_protocol.py, which only updates when explicitly polled.

Report layout (Firmware/FFBoard/Inc/ffb_defs.h, reportHID_t, packed):
    byte 0      : report id
    bytes 1-8   : buttons (uint64 LE) - one bit per enabled ButtonSource, packed
                  from bit 0 upward in ascending class-id order (see
                  SelectableInputs::getButtonValues() in the firmware)
    bytes 9-10  : X  (int16 LE) - axis 0's scaled position -> "Degree x-Achse"
    bytes 11-12 : Y  (int16 LE) - first enabled local analog channel -> "Value analog 1"
    bytes 13-14 : Z  (int16 LE) - second enabled local analog channel -> "Value analog 2"

This is purely an optional enhancement: if the `hidapi` package or the HID
interface itself is unavailable, connect() reports failure via on_log and the
caller keeps using the existing serial polling instead.
"""
import queue
import struct
import threading

try:
    import hid
except ImportError:
    hid = None

VID_PID = (0x1209, 0xFFB0)


class HidLink:
    def __init__(self, on_report, on_log):
        self.on_report = on_report
        self.on_log = on_log
        self.device = None
        self.thread = None
        self.running = False
        self.queue = queue.Queue()
        self.connected = False

    def connect(self):
        if hid is None:
            self.on_log("HID interface unavailable (package 'hidapi' missing), using serial polling")
            return False
        try:
            device = hid.device()
            device.open(*VID_PID)
            device.set_nonblocking(False)
        except Exception as exc:
            self.on_log(f"HID interface unavailable ({exc}), using serial polling")
            return False

        self.device = device
        self.running = True
        self.thread = threading.Thread(target=self._read_loop, daemon=True)
        self.thread.start()
        self.connected = True
        return True

    def disconnect(self):
        self.running = False
        self.connected = False
        if self.device is not None:
            try:
                self.device.close()
            except Exception:
                pass
        self.device = None
        while True:
            try:
                self.queue.get_nowait()
            except queue.Empty:
                break

    def _read_loop(self):
        while self.running:
            try:
                data = self.device.read(64)
            except Exception:
                return
            if data and len(data) >= 15:
                buttons, x, y, z = struct.unpack_from("<Qhhh", bytes(data), 1)
                self.queue.put((buttons, x, y, z))

    def pump(self):
        """Drain queued reports and dispatch the latest one. Call from the GUI thread."""
        latest = None
        while True:
            try:
                latest = self.queue.get_nowait()
            except queue.Empty:
                break
        if latest is not None:
            self.on_report(*latest)
