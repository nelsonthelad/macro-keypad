import usb_hid
import digitalio
import time
import board

# This is the tester file to ensure that all the buttons and rotary encoder are working

# Setting up the buttons

buttons = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11]
key = [digitalio.DigitalInOut(pin_name) for pin_name in buttons]
for x in range(len(buttons)):
    key[x].direction = digitalio.Direction.INPUT
    key[x].pull = digitalio.Pull.DOWN

# Setting up the rotary encoder
    
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

# Rotary Encoder Variables
previousValue1 = CLK_Pin1.value
previousValue2 = CLK_Pin2.value

def rotary_changed(clk_pin, dt_pin, previous_value):
    clk_state = clk_pin.value
    if previous_value != clk_state:
        if clk_state == 0:
            return dt_pin.value == 1
    return None

# Main loop

while True:
    for i in range(len(key)):
        if key[i].value:
            print(i)
            time.sleep(0.2)
    
    result1 = rotary_changed(CLK_Pin1, DT_Pin1, previousValue1)
    result2 = rotary_changed(CLK_Pin2, DT_Pin2, previousValue2)
    
    if result1 is not None:
        print("Encoder 1:", "left" if result1 else "right")
    if result2 is not None:
        print("Encoder 2:", "left" if result2 else "right")
    
    previousValue1 = CLK_Pin1.value
    previousValue2 = CLK_Pin2.value
    
    if not SW1.value:
        print("Rotary 1 Click")
        time.sleep(0.2)
    
    if not SW2.value:
        print("Rotary 2 Click")
        time.sleep(0.2)
    
    time.sleep(0.01)