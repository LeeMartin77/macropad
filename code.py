import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

kbd = Keyboard(usb_hid.devices)

pin_key_array = [
    (digitalio.DigitalInOut(board.GP1), Keycode.ONE),
    (digitalio.DigitalInOut(board.GP2), Keycode.TWO),
    (digitalio.DigitalInOut(board.GP3), Keycode.THREE),
    (digitalio.DigitalInOut(board.GP4), Keycode.FOUR),
    (digitalio.DigitalInOut(board.GP5), Keycode.FIVE),
    (digitalio.DigitalInOut(board.GP6), Keycode.SIX),
    (digitalio.DigitalInOut(board.GP7), Keycode.SEVEN),
    (digitalio.DigitalInOut(board.GP8), Keycode.EIGHT),
    (digitalio.DigitalInOut(board.GP9), Keycode.NINE)
]

for pin_key in pin_key_array:
    pin_key[0].direction = digitalio.Direction.INPUT
    pin_key[0].pull = digitalio.Pull.DOWN

while True:
    for pin_key in pin_key_array:
        if pin_key[0].value:
            kbd.press(pin_key[1])
    time.sleep(0.1)
    kbd.release_all()

