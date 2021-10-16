import time
import board
import digitalio
import usb_hid

# from adafruit_hid.keyboard import Keyboard
# from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

# kbd = Keyboard(usb_hid.devices)
control = ConsumerControl(usb_hid.devices)

# Soldered Layout:
# -------------------
# | GP1 | GP2 | GP3 |
# -------------------
# | GP4 | GP5 | GP6 |
# -------------------
# | GP7 | GP8 | GP9 |
# -------------------

pin_key_single_array = [
    (digitalio.DigitalInOut(board.GP1), ConsumerControlCode.VOLUME_INCREMENT, False),
    (digitalio.DigitalInOut(board.GP2), ConsumerControlCode.SCAN_PREVIOUS_TRACK, True),
    (digitalio.DigitalInOut(board.GP3), ConsumerControlCode.SCAN_NEXT_TRACK, True),
    (digitalio.DigitalInOut(board.GP4), ConsumerControlCode.VOLUME_DECREMENT, False),
    (digitalio.DigitalInOut(board.GP5), ConsumerControlCode.PLAY_PAUSE, True),
    # (digitalio.DigitalInOut(board.GP6), None),
    (digitalio.DigitalInOut(board.GP7), ConsumerControlCode.MUTE, True),
    # (digitalio.DigitalInOut(board.GP8), None),
    # (digitalio.DigitalInOut(board.GP9), None)
]

for (pin, key, single) in pin_key_single_array:
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.DOWN

while True:
    for (pin, key, single) in pin_key_single_array:
        if pin.value:
            control.press(key)
            # If it's a single key, wait til the key is released before doing anything else
            while single and pin.value:
                pass
            time.sleep(0.1)
            control.release()
