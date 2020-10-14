#!/bin/env python3

import RPi.GPIO as GPIO
import time

def callback(channel):
        if GPIO.input(channel):
                print("LED off")
        else:
                print("LED on")

GPIO.setmode(GPIO.BCM)

channel = 17
GPIO.setup(channel, GPIO.IN)

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

while True:
        time.sleep(0.1)
