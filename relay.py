#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

relay1_gpio = 26
GPIO.setup(relay1_gpio, GPIO.OUT)

def relay1_on():
  GPIO.setup(relay1_gpio, GPIO.OUT) # GPIO Assign Mode
  GPIO.output(relay1_gpio, GPIO.LOW) # Low signal closes relay loop

def relay1_off():
  GPIO.setup(relay1_gpio, GPIO.OUT)
  GPIO.output(relay1_gpio, GPIO.HIGH)

def relay_loop():
  relay1_on()
  sleep(5)
  relay1_off()
  sleep(5)

# while True:
#   relay_loop()

state = GPIO.input(relay1_gpio)

if state == 0:
  relay1_off()
else:
  relay1_on()
