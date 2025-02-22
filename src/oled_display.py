import board, busio, displayio, terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect

import time

class OLEDDisplay:
    def __init__(self):
        self.splash = displayio.Group()
        self.display = None
        self.header_box = None
        self.header_text = None
        self.header_displayed = False
        self.macro_label = None
    
    def initialize(self):
        displayio.release_displays()

        sda, scl = board.GP16, board.GP17  
        i2c = busio.I2C(scl, sda)
        display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

        self.display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

        # Assign splash to self.splash
        self.splash = displayio.Group()

        color_bitmap = displayio.Bitmap(128, 64, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = 0x000000

        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
        self.splash.append(bg_sprite)

        self.display.root_group = self.splash
        
    def clear(self):
        self.display.fill(0)
        
    def setMacroLabel(self, text, x_cord, y_cord):
        self.macro_label = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=x_cord, y=y_cord)
        self.splash.append(self.macro_label)
        
    def clearMacroLabel(self):
        if self.macro_label:
            self.splash.remove(self.macro_label)
        
    def drawHeader(self):
        self.header_displayed = True
        self.header_box = Rect(0, 0, 128, 22, outline=0xFFFFFF, stroke=2)  
        self.header_text = label.Label(terminalio.FONT, text="Welcome Nelson!", color=0xFFFFFF, x=20, y=10)
            
        self.splash.append(self.header_box)  
        self.splash.append(self.header_text)

    def clearHeader(self):
        if self.header_displayed is True: 
            self.splash.remove(self.header_box)
            self.splash.remove(self.header_text)
            self.header_displayed = False