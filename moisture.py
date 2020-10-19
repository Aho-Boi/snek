#!/bin/env python3

import RPi.GPIO as GPIO
import time

def callback(channel):
        if GPIO.input(channel):
                print("LED off")
        else:
                print("LED on")

def init_moist(pin):
  GPIO.setmode(GPIO.BCM)
  channel = pin
  GPIO.setup(channel, GPIO.IN)

def launch_moist():
  GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
  GPIO.add_event_callback(channel, callback)
  while True:
        time.sleep(0.1)
