#!/usr/bin/python3
from time import *
import RPi.GPIO as GPIO
import Adafruit_DHT
from libraries import relay

sensor = Adafruit_DHT.DHT22
pin = 22

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
sleep(2)
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    #humidity = float(humidity)
    #temperature = float(temperature)

    if humidity > 20.0 or temperature > 24.0:
        relay.relay1_on()
    
    else: 
        relay.relay1_off()

else:
    print("Nothing to do")
