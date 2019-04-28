#!/usr/bin/python3

import sensor_functions as sensor
import RPi.GPIO as GPIO

while True:

  try:
    sensor.temp_update()
    sensor.fan_check()
    sensor.get_distance()

  except:
    sensor.lcd_shutdown()
    GPIO.cleanup()
    break

