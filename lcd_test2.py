#!/usr/bin/python3

import sensor_functions as sensor
import RPi.GPIO as PINS

while True:

  try:
    sensor.temp_update()
    sensor.fan_check()
    sensor.get_distance()

  except:
    sensor.lcd_shutdown()
    PINS.cleanup()
    break

