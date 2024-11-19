#This is written in MicroPython for a rasp Pi Micro to display an encoders position on an SSD1306 OLED display.

from machine import Pin, I2C
import ssd1306
import time

# I2C setup for OLED
i2c = I2C(0, scl=Pin(9), sda=Pin(8)) 
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

#for rotary encoder
pin_clk = Pin(2, Pin.IN, Pin.PULL_UP)
pin_dt = Pin(3, Pin.IN, Pin.PULL_UP)
pin_sw = Pin(4, Pin.IN, Pin.PULL_UP)

encoder_pos = 0
last_state_clk = pin_clk.value()

def read_encoder():
    global last_state_clk, encoder_pos
    state_clk = pin_clk.value()
    state_dt = pin_dt.value()
    if state_clk != last_state_clk:
        if state_dt != state_clk:
            encoder_pos += 1
        else:
            encoder_pos -= 1
        oled.fill(0)  #Clear the display
        oled.text('Pos: {}'.format(encoder_pos), 0, 0)
        oled.show()
    last_state_clk = state_clk

def button_press():
    while pin_sw.value() == 0:
        pass  #Wait for button release
    print("Button pressed!")

try:
    while True:
        read_encoder()
        if pin_sw.value() == 0:  #Check if button is pressed
            button_press()
        time.sleep(0.01)  

except KeyboardInterrupt:
    pass
