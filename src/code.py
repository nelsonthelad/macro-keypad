import board, busio, displayio, os, terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
import usb_hid
import digitalio
import time
import rotaryio
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

from oled_display import OLEDDisplay
import macro

cc = ConsumerControl(usb_hid.devices)
        
# ------- Button Setup --------

buttons = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11]
key = [digitalio.DigitalInOut(pin_name) for pin_name in buttons]
for x in range(len(buttons)):
    key[x].direction = digitalio.Direction.INPUT
    key[x].pull = digitalio.Pull.DOWN
    
# ----- Rotary Encoder Setup -----

DT_Pin1 = digitalio.DigitalInOut(board.GP12)
DT_Pin1.direction = digitalio.Direction.INPUT
DT_Pin1.pull = digitalio.Pull.DOWN

CLK_Pin1 = digitalio.DigitalInOut(board.GP13)
CLK_Pin1.direction = digitalio.Direction.INPUT
CLK_Pin1.pull = digitalio.Pull.DOWN

SW1 = digitalio.DigitalInOut(board.GP14)
SW1.direction = digitalio.Direction.INPUT
SW1.pull = digitalio.Pull.UP

DT_Pin2 = digitalio.DigitalInOut(board.GP19)
DT_Pin2.direction = digitalio.Direction.INPUT
DT_Pin2.pull = digitalio.Pull.DOWN

CLK_Pin2 = digitalio.DigitalInOut(board.GP20)
CLK_Pin2.direction = digitalio.Direction.INPUT
CLK_Pin2.pull = digitalio.Pull.DOWN

SW2 = digitalio.DigitalInOut(board.GP15)
SW2.direction = digitalio.Direction.INPUT
SW2.pull = digitalio.Pull.UP  

previousValue1 = CLK_Pin1.value
previousValue2 = CLK_Pin2.value

def rotary_changed(clk_pin, dt_pin, previous_value):
    clk_state = clk_pin.value
    if previous_value != clk_state:
        if clk_state == 0:
            return dt_pin.value == 1
    return None

# -------- Display -------

dis = OLEDDisplay()

dis.initialize()
dis.drawHeader()

# --- Main Loop ---

while True:
    if key[0].value:
        macro.key1()
        dis.clearMacroLabel()
        dis.setMacroLabel("Copied", 15, 30)
        
    if key[1].value:
        macro.key2()
        dis.clearMacroLabel()
        dis.setMacroLabel("Pasted", 15, 30)
        
    if key[2].value:
        macro.key3()
        dis.clearHeader()
        
    if key[3].value:
        macro.key4()
        dis.drawHeader()
        
    if key[4].value:
        macro.key5()
        
    if key[5].value:
        macro.key6()
        
    if key[6].value:
        macro.key7()
        
    if key[7].value:
        macro.key8()
            
    if key[8].value:
        macro.key9()
        
    if key[9].value:
        macro.key10()
        
    if key[10].value:
        macro.key11()
    
    result1 = rotary_changed(CLK_Pin1, DT_Pin1, previousValue1)
    result2 = rotary_changed(CLK_Pin2, DT_Pin2, previousValue2)
    
    if result1 is not None:
        if result1:
            cc.press(ConsumerControlCode.VOLUME_INCREMENT)
            print("Volume Up")
            cc.release()
        else:
            cc.press(ConsumerControlCode.VOLUME_DECREMENT)
            print("Volume Down")
            cc.release()
        
    if result2 is not None:
        print("Encoder 2:", "left" if result2 else "right")
    
    previousValue1 = CLK_Pin1.value
    previousValue2 = CLK_Pin2.value
    
    if not SW1.value:
        print("Rotary 1 Click")
        time.sleep(0.01)
     
    if not SW2.value:
        print("Rotary 2 Click")
        time.sleep(0.01)
    
    time.sleep(0.01)