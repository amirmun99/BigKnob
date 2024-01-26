import time
import board
import digitalio
import rotaryio
import random
from adafruit_ssd1306 import SSD1306_I2C
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# OLED Setup
WIDTH = 128
HEIGHT = 64
i2c = board.I2C()
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Rotary Encoder Setup
encoder = rotaryio.IncrementalEncoder(board.A2, board.A3)
last_position = encoder.position
switch = digitalio.DigitalInOut(board.A1)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# HID Consumer Control Setup
consumer_control = ConsumerControl(usb_hid.devices)

# Bitmaps
mute_icon = [
    0b00111100,
    0b01111110,
    0b11100111,
    0b11011011,
    0b11011011,
    0b11100111,
    0b01111110,
    0b00111100,
]

up_arrow = [
    0b00100,
    0b01110,
    0b11111,
    0b00100,
    0b00100,
    0b00100,
    0b00100,
    0b00100,
    0b00100,
    0b00100 
]

down_arrow = [
    0b00100,
    0b00100,
    0b00100,
    0b00100,
    0b00100,
    0b00100,
    0b00100,
    0b11111,
    0b01110,
    0b00100
]

unmute_icon = [  # Circle for unmute
    0b00111100,
    0b01100110,
    0b11000011,
    0b11000011,
    0b11000011,
    0b11000011,
    0b01100110,
    0b00111100
]

# Function to display bitmap
def display_bitmap(bitmap, width, height, x_offset, y_offset):
    oled.fill(0)
    for y, row in enumerate(bitmap):
        for x in range(width):
            if row & (1 << (width - 1 - x)):
                oled.pixel(x + x_offset, y + y_offset, 1)
    oled.show()

# Function for Matrix-style animation
def matrix_animation():
    oled.fill(0)
    columns = WIDTH // 6
    drops = [0 for _ in range(columns)]

    while True:
        for i in range(columns):
            x = i * 6
            y = drops[i] * 8
            char = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*')
            oled.text(char, x, y, 1)
            drops[i] += 1
            if drops[i] * 8 > HEIGHT or random.random() > 0.85:  # Increased randomness
                drops[i] = 0

        oled.show()
        time.sleep(0.05)  # Increased speed
        oled.fill(0)

        if encoder.position != last_position or not switch.value:
            break

# Main Loop
volume = 100
is_muted = False
last_interaction_time = time.monotonic()

while True:
    position = encoder.position
    current_time = time.monotonic()

    if position != last_position:
        delta = position - last_position
        last_position = position
        volume = max(0, min(100, volume + delta))
        last_interaction_time = current_time

        arrow_bitmap = up_arrow if delta > 0 else down_arrow
        display_bitmap(arrow_bitmap, 5, 5, (WIDTH - 5) // 2, (HEIGHT - 5) // 2)

        if delta > 0:
            consumer_control.send(ConsumerControlCode.VOLUME_INCREMENT)
        elif delta < 0:
            consumer_control.send(ConsumerControlCode.VOLUME_DECREMENT)

    if not switch.value:  # Button is pressed
        is_muted = not is_muted
        icon = mute_icon if is_muted else unmute_icon
        display_bitmap(icon, 8, 8, (WIDTH - 8) // 2, (HEIGHT - 8) // 2)
        consumer_control.send(ConsumerControlCode.MUTE)
        time.sleep(0.2)
        last_interaction_time = current_time

    if current_time - last_interaction_time > 2:
        matrix_animation()
        last_interaction_time = current_time
