from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.mouse import Mouse
import usb_hid
import time

#----- Setup all the Devices ------

mouse = Mouse(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

#----- Debounce Time -----

debounce_time = 0.2

def debounce():
    time.sleep(debounce_time)

#----- Functions For Each Key -----
    
def key1():
    kbd.press(Keycode.COMMAND)
    kbd.press(Keycode.C)
    kbd.release_all()
    debounce()
    
def key2():
    kbd.press(Keycode.COMMAND)
    kbd.press(Keycode.V)
    kbd.release_all()
    debounce()
    
def key3():
    debounce()

def key4():
    debounce()

def key5():
    kbd.send(Keycode.CONTROL, Keycode.V)

def key6():
    layout.write("Hello, World!")

def key7():
    mouse.move(x=10)

def key8():
    mouse.move(x=-10)

def key9():
    mouse.move(y=-10)

def key10():
    mouse.move(y=10)

def key11():
    kbd.send(Keycode.ENTER)