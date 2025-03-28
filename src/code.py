import board, busio, displayio, os, terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
import usb_hid
import digitalio
import time
import rotaryio
import storage, usb_cdc

from oled_display import OLEDDisplay
import macro


#---- Boot Mode ----

#shutOff = digitalio.DigitalInOut(board.GP18)
#shutOff.direction = digitalio.Direction.INPUT
#shutOff.pull = digitalio.Pull.UP

#if shutOff.value:
    #storage.disable_usb_drive()
    #usb_cdc.disable()

        
# ------- Button Setup --------

buttons = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11]
key = [digitalio.DigitalInOut(pin_name) for pin_name in buttons]
for x in range(len(buttons)):
    key[x].direction = digitalio.Direction.INPUT
    key[x].pull = digitalio.Pull.DOWN
    
# ----- Rotary Encoder Setup -----

encoder1 = rotaryio.IncrementalEncoder(board.GP13, board.GP12)
encoder2 = rotaryio.IncrementalEncoder(board.GP20, board.GP19)

SW1 = digitalio.DigitalInOut(board.GP14)
SW1.direction = digitalio.Direction.INPUT
SW1.pull = digitalio.Pull.UP

SW2 = digitalio.DigitalInOut(board.GP15)
SW2.direction = digitalio.Direction.INPUT
SW2.pull = digitalio.Pull.UP  

last_position1 = encoder1.position
last_position2 = encoder2.position

# -------- Display -------

dis = OLEDDisplay()

dis.initialize()
dis.drawHeader()

# --- Main Loop ---

while True:
    if key[0].value:
        macro.key1()
        dis.clearMacroLabel()
        dis.setMacroLabel("Copied", 45, 45)
        
    if key[1].value:
        macro.key2()
        dis.clearMacroLabel()
        dis.setMacroLabel("Pasted", 45, 45)
        
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
    
    # ----- Rotary Encoders ----
    current_position1 = encoder1.position
    if current_position1 > last_position1:
        macro.r1up()
        dis.clearMacroLabel()
        dis.setMacroLabel("Volume Up!", 38, 45)
    elif current_position1 < last_position1:
        macro.r1down()
        dis.clearMacroLabel()
        dis.setMacroLabel("Volume Down!", 34, 45)
    last_position1 = current_position1
    
    current_position2 = encoder2.position
    if current_position2 > last_position2:
        macro.r2up()
        dis.clearMacroLabel()
        dis.setMacroLabel("Zoomed In!", 38, 45)
    elif current_position2 < last_position2:
        macro.r2down()
        dis.clearMacroLabel()
        dis.setMacroLabel("Zoomed Out!", 38, 45)
    last_position2 = current_position2
    
    if not SW1.value:
        macro.sw1()
        dis.clearMacroLabel()
        dis.setMacroLabel("Muted!", 45, 45)
     
    if not SW2.value:
        macro.sw2()
        dis.clearMacroLabel()
        dis.setMacroLabel("Set to Original Size", 30, 45)
        
    time.sleep(0.005)