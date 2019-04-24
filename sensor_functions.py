#!/usr/bin/python3

from libraries import I2C_LCD_driver as lcd_lib
import Adafruit_DHT
import distance as dst
from time import *

# Define LCD panel
mylcd = lcd_lib.lcd()


# Get temp and humidity update, display for 30 secs, clear screen
def temp_update():

    sensor = Adafruit_DHT.DHT22
    pin = 22

    mylcd.lcd_display_string('Taking environmental', 1)
    mylcd.lcd_display_string('Readings now.', 2)
    mylcd.lcd_display_string('...', 3)
    mylcd.lcd_display_string('Please wait.', 4)

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    sleep(2)
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    mylcd.lcd_clear()

    if humidity is not None and temperature is not None:
        mylcd.lcd_display_string('Temperature = {0:0.1f}*C'.format(temperature), 1)
        sleep(0.5)
        mylcd.lcd_display_string('Humidity = {0:0.1f}%'.format(humidity), 2)
    else:
        mylcd.lcd_display_string('Failed to get', 1)
        mylcd.lcd_display_string('reading from DHT22', 2)

    sleep(30)
    mylcd.lcd_clear()

# Get distance reading
def get_distance():

    # Print results to LCD
    mylcd.lcd_display_string("Calculating Distance", 1)
    sleep(1)
    mylcd.lcd_display_string("...", 2)
    sleep(1)
    mylcd.lcd_display_string(dst.get_distance(), 4)
    sleep(10)
    mylcd.lcd_clear()

# Process to shutdown LCD in 'except' block
def lcd_shutdown():

    mylcd.lcd_clear()

    mylcd.lcd_display_string('Temp updates now', 1)
    mylcd.lcd_display_string('Shutting down', 2)
    mylcd.lcd_display_string('...', 3)

    sleep(2)
    mylcd.lcd_display_string('Goodbye!', 4)

    sleep(5)
    mylcd.lcd_clear()