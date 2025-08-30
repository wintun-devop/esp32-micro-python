
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