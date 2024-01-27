# BigKnob
"Big Knob" is a Physical volume control knob with an OLED Screen. Utilizing a 3D Printed case and running on a SEEED XIAO RP2040. The screen is mostly cosmetic, displaying a matrix style animation during inactivity and providing realtime feedback about the input being sent to the PC.


---

## Required Libraries

To run the provided script, you'll need several libraries. Here's where to find them:

- **Adafruit SSD1306**: For OLED display control. Download from [Adafruit's GitHub](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306) or the CircuitPython Library Bundle.
- **Adafruit HID**: For Human Interface Device control. Download from [Adafruit's GitHub](https://github.com/adafruit/Adafruit_CircuitPython_HID) or the CircuitPython Library Bundle.
- **Adafruit_Framebuf**: Found in the Adafruit CircuitPython Bundle. Download From https://circuitpython.org/libraries

## Hardware Required

You will need the following hardware components:

- **XIAO RP2040**: A powerful microcontroller from Seeed Studio.
- **EC11 Rotary Encoder**: For volume control input.
- **OLED Display**: Specifically, an SSD1306 OLED display compatible with the Adafruit SSD1306 library.
- **3D Printed Case**: To house the components neatly. Designs can be found in the repository or on Printables. The Case requires 4 6x3mm round magnets.

## Software 

I recommend using **Thonny**, an Integrated Development Environment (IDE) that is beginner-friendly and supports CircuitPython. It provides a straightforward way to write, deploy, and debug your code on the XIAO RP2040.

## Installation Guide

### Installing CircuitPython

1. Download the latest CircuitPython firmware for the XIAO RP2040 from the [CircuitPython Downloads page](https://circuitpython.org/board/seeeduino_xiao_rp2040/).
2. Connect the XIAO RP2040 to your computer.
3. Enter bootloader mode by Holding the BOOT button and plugging the device into your PC.
4. A drive named `RPI-RP2` should appear. Drag and drop the CircuitPython `.uf2` file onto this drive.
5. The device will reboot and mount a new drive named `CIRCUITPY`.

### Installing Libraries

1. Create a folder named `lib` on the `CIRCUITPY` drive if it doesn't already exist.
2. Download the required libraries from the provided links or this repository.
3. Copy the library files into the `lib` folder on the `CIRCUITPY` drive.

### Installing the Code

1. Copy the Python script provided above to the main directory of the `CIRCUITPY` drive.
2. Rename the script to `code.py`.
3. The device automatically executes `code.py` when powered on or reset.

## Usage

- **Volume Control**: Rotate the knob to increase or decrease the volume.
- **Mute/Unmute**: Press the knob to toggle between mute and unmute.
- **Display**: When not interacting with the knob, the OLED will display a matrix-style animation. Icons will appear during interaction to indicate volume changes or mute status.
