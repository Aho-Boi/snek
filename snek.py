#!/bin/env python3
from dht import *
from moisture import *
from relay import *

def init_sensor(pin_relay,pin_moist):
  init_dht()
  init_relay(pin_relay)
  init_moist(pin_moist)

def launch_lamp(temp):
  if (temp <= 35):
    switch_lamp(True)
  else :
    switch_lamp(False)

def temp_loop():
  while True:
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} C    Humidity: {}% ".format(
            temperature_c, humidity
            )
        )
        launch_lamp(temperature_c)

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)

def main():
  init_sensor(4,14)
  temp(loop)

if __name__ == "__main__":
  main()
