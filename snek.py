#!/bin/env python3
from dht import *
# from moisture import *

import time
import board
import adafruit_dht
import RPi.GPIO as GPIO

dhtDevice = adafruit_dht.DHT11(board.D18)
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers

RELAIS_1_GPIO = 4
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode

BUZZER_PIN = 12
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.output(BUZZER_PIN, GPIO.HIGH) #on

def switch_lamp(var):
  if(var):
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) #on
  else:
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out

def init_sensor(pin_relay,pin_moist):
    pass
    # dhtDevice = init_dht()
    #init_moist(pin_moist)

def buzz():
    print("buzzed")
    GPIO.output(BUZZER_PIN, GPIO.LOW) # out
    time.sleep(0.1)
    GPIO.output(BUZZER_PIN, GPIO.HIGH) #on

buzzed = False
def launch_lamp(temp):
    global buzzed
    if (temp <= 40):
        switch_lamp(True)
        buzzed = False
    else :
        switch_lamp(False)
        if not buzzed:
            buzz()
            buzzed = True

def temp_loop():
  while True:
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print(f"Temp: {temperature_c:.1f} c\tHumidity: {humidity}%\t{buzzed}")
        launch_lamp(humidity)

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        # dhtDevice.exit()
        raise error

    time.sleep(2.0)

def main():
  init_sensor(4,14)
  temp_loop()

if __name__ == "__main__":
  main()
