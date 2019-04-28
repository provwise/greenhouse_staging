#!/usr/bin/python3
from time import *
import RPi.GPIO as GPIO
import Adafruit_DHT
from libraries import relay

sensor = Adafruit_DHT.DHT22
pin = 22
state = GPIO.input(37)

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
sleep(2)
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    #humidity = float(humidity)
    #temperature = float(temperature)

    if (humidity > 20.0 or temperature > 24.0) and state == 1:
        relay.relay1_on()
        print("Ventilation system turned on")
        print("Temperature: %.2f" % (temperature))
        print("Humidity: %.2f" % (humidity))
    
    elif (humidity < 20.0 or temperature < 24.0) and state == 0: 
        relay.relay1_off()
        print("Ventilation system turned off")
        print("Temperature: %.2f" % (temperature))
        print("Humidity: %.2f" % (humidity))

    else:
        print("No change to ventilation status needed")


else:
    print("Could not get temperature or humidity readings.")
