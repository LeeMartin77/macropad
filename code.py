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

apin = digitalio.DigitalInOut(board.GP1)
apin.direction = digitalio.Direction.INPUT
apin.pull = digitalio.Pull.DOWN

while True:
    if apin.value:
        led.value = not led.value
        kbd.press(Keycode.A)
    time.sleep(0.1)
    kbd.release_all()

