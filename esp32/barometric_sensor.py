import time,sys,machine,ubinascii,os
from machine import Pin,I2C
from time import sleep
from bmp180 import BMP180


#build in led for operation status
led = Pin(2, Pin.OUT)
# Initialize I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
import os


# BMP180 address is typically 0x77
sensor = BMP180(i2c)

# Optionally adjust sea level pressure for more accurate altitude readings
# bmp.sealevel_pressure = 101325

def main():
    while True:
        print("start")
        led.value(1) # led ON
        #Read sensor data
        print("i2c",i2c)
        print("osdir",os.listdir())
        # print("sensor",sensor)
        temperature = sensor.temperature
        pressure = sensor.pressure
        altitude = sensor.altitude
        print("Temperature:", temperature, "°C")
        print("Pressure:", pressure, "Pa")
        print("Altitude:", altitude, "m")
        #led OFF
        led.value(0) 
        sleep(1)



def get_machine_id()->str:
    machine_id = str(ubinascii.hexlify(machine.unique_id()).decode())
    return machine_id

if __name__ == "__main__":
    main()

""" 
from machine import I2C, Pin
from bmp180 import BMP180
from time import sleep

# Initialize I2C (adjust pins as needed for your board)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

# BMP180 address is typically 0x77
bmp = BMP180(i2c, addr=0x77)

# Optionally adjust sea level pressure for more accurate altitude readings
# bmp.sealevel_pressure = 101325

while True:
    # Read temperature and pressure
    temp = bmp.temperature
    pressure = bmp.pressure
    altitude = bmp.altitude

    print("Temperature: {:.2f} °C".format(temp))
    print("Pressure: {:.2f} hPa".format(pressure / 100)) # Convert Pa to hPa
    print("Altitude: {:.2f} m".format(altitude))
    sleep(1)

"""

# micro python 
#https://github.com/micropython-IMU
