#!/bin/env python3

import time
import sys
import board
import adafruit_dht
import argparse
import RPi.GPIO as GPIO

RELAIS_1_GPIO = 4
BUZZER_GPIO = 12
dhtDevice = adafruit_dht.DHT11(board.D18)

def toggle_lamp():
    if GPIO.input(RELAIS_1_GPIO) == GPIO.LOW:
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
    else:
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW)

def buzz():
    GPIO.output(BUZZER_GPIO, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(BUZZER_GPIO, GPIO.HIGH)

def get_temp():
    return dhtDevice.temperature

def get_humidity():
    return dhtDevice.humidity

def create_parser():
    parser = argparse.ArgumentParser(description="Give infos about GPIOS status")
    parser.add_argument("-t", "--temperature", action="store_true",
            help="Give the temperature")
    parser.add_argument("-u", "--humidity", action="store_true",
            help="Give the humidity")
    parser.add_argument("-l", "--toggle_lamp", action="store_true",
            help="Toggle the lamp")
    parser.add_argument("-b", "--buzz", action="store_true",
            help="Give the buzz")
    return parser

def main(argv):
    GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
    GPIO.setup(BUZZER_GPIO, GPIO.OUT)
    GPIO.output(BUZZER_GPIO, GPIO.HIGH) # Default as High

    args = create_parser().parse_args(argv[1:])
    if args.temperature:
        print(get_temp())
    if args.humidity:
        print(get_humidity())
    if args.toggle_lamp:
        toggle_lamp()
    if args.buzz:
        buzz()

if __name__ == "__main__":
  main(sys.argv)
