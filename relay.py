#!/bin/env python3

import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers

RELAIS_1_GPIO = 04
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
GPIO.setwarnings(False)

SLEEP_TIME = 1
while True:
    time.sleep(SLEEP_TIME)
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
    time.sleep(SLEEP_TIME)
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) #on
