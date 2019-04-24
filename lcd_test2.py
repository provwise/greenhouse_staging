#!/usr/bin/python3

import sensor_functions as sensor

while True:

  try:
    sensor.temp_update()
    sensor.get_distance()

  except:
    sensor.lcd_shutdown()
    break
