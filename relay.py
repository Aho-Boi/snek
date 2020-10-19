#!/bin/env python3

import time

import RPi.GPIO as GPIO

def init_relay(pin):
  GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers

  RELAIS_1_GPIO = pin
  GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
  GPIO.setwarnings(False)

def switch_lamp(var)
  if(var):
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) #on
  else:  
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
