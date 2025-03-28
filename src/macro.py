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
rotary_debounce_time = 0.01

def debounce():
    time.sleep(debounce_time)
    
def rotaryDebounce():
    time.sleep(rotary_debounce_time)

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
    debounce()

def key6():
    layout.write("Hello, World!")

def key7():
    debounce()

def key8():
    debounce()

def key9():
    debounce()

def key10():
    debounce()

def key11():
    debounce()

def sw1():
    cc.press(ConsumerControlCode.MUTE)
    cc.release()
    debounce()
    
def sw2():
    kbd.press(Keycode.COMMAND)
    kbd.press(Keycode.O)
    kbd.release_all()
    debounce()
    
def r1up():
    cc.press(ConsumerControlCode.VOLUME_INCREMENT)
    cc.release()
    rotaryDebounce()
    
def r1down():
    cc.press(ConsumerControlCode.VOLUME_DECREMENT)
    cc.release()
    rotaryDebounce()
    
def r2up():
    kbd.press(Keycode.COMMAND)
    kbd.press(Keycode.SHIFT)
    kbd.press(Keycode.EQUALS)
    kbd.release_all()
    rotaryDebounce()
    
def r2down():
    kbd.press(Keycode.COMMAND)
    kbd.press(Keycode.SHIFT)
    kbd.press(Keycode.MINUS)
    kbd.release_all()
    rotaryDebounce()