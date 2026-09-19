# Twisty-OpenFFBoard-GUI

A standalone Windows desktop configurator for the [Twisty-OpenFFBoard-Firmware](https://github.com/EmanresuEmanreztuneb/Twisty-OpenFFBoard-Firmware), a custom [OpenFFBoard](https://github.com/Ultrawipf/OpenFFBoard) fork for a VESC-driven DIY force-feedback steering wheel / wheelbase.

> 🎬 **Demo GIF placeholder** — a short animation of the GUI in action goes here. Replace this line with `![Twisty GUI demo](docs/demo.gif)` once `docs/demo.gif` is added.

## Download (no Python required)

Grab the latest `Twisty_FFBoard_GUI.exe` from the [Releases page](../../releases). It's a self-contained Windows executable — just download it and double-click, no Python installation or extra dependencies needed.

## Features

- Live configuration of the wheel: rotation range, power, endstop, invert axis, center position.
- Analog input calibration (min/max, invert) with live sliders for the two auxiliary analog channels (accelerate/brake).
- Digital button mapping display for the local button inputs.
- Force-feedback effect tuning: spring, friction, damper, inertia, plus per-effect response-curve graphs and biquad filter tuning in the Advanced tab.
- Live readouts: VESC supply voltage, temperature, and the firmware's PT100 over-temperature protection stage.
- Save/load full configuration profiles (`.twisty` files) to a plain-text file.
- Communicates with the board over USB-CDC serial (115200 baud) plus a USB HID channel for low-latency live values.

## Running from source

If you'd rather run it from source instead of the packaged `.exe`:

```
pip install -r requirements.txt
python main.py
```

Dependencies: `pyserial`, `Pillow`, `hidapi`.

## Building the executable yourself

The packaged `.exe` is built with PyInstaller using the included spec file:

```
pyinstaller Twisty_FFBoard_GUI.spec
```

## Credits

This is a reduced, purpose-built reimplementation of the official [OpenFFBoard-configurator](https://github.com/Ultrawipf/OpenFFBoard-configurator) by Yannick Richter ("Ultrawipf") and contributors, tailored specifically to the Twisty/VESC configuration. It reuses functionality and protocol logic from the original configurator, with a fully custom interface.

## License

This project is licensed under the **GNU General Public License v3.0** — see [LICENSE](LICENSE). It is a derivative work of the GPLv3-licensed `OpenFFBoard-configurator`, so it is distributed under the same license, including the full corresponding source code.
