
import uasyncio as asyncio
import os
from machine import SoftI2C, Pin

# i2c = SoftI2C(scl=Pin(7), sda=Pin(6))
sda_pins = [4, 21, 18]
scl_pins = [5, 22, 19]



async def run_server():
    while True:
        for sda in sda_pins:
            for scl in scl_pins:
                try:
                    i2c = SoftI2C(scl=Pin(scl), sda=Pin(sda))
                    devices = i2c.scan()
                    print(f"SDA={sda}, SCL={scl} → {devices}")
                except Exception as e:
                    print(f"Error with SDA={sda}, SCL={scl}: {e}")
        await asyncio.sleep(1)


async def main():
    await run_server()

asyncio.run(main())

""" 
# output
SDA=4, SCL=5 → [] 
SDA=4, SCL=22 → [] 
SDA=4, SCL=19 → [] 
SDA=21, SCL=5 → [
8, 9, 10, 11, 12, 
13, 14, 15, 16, 17, 18, 19, 20,
 21, 22, 23, 24, 25, 26, 27, 28, 
 29, 30, 31, 32, 33, 34, 35, 36, 37, 
 38, 39, 40, 41, 42, 43, 44, 45, 46, 
 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 
 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 
 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78,
 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,
101, 102, 103, 104, 105, 106, 107,
108, 109, 110, 111, 112, 113, 114, 
115, 116, 117, 118, 119]




 """