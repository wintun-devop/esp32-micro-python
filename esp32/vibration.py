# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

from machine import Pin
import uasyncio as asyncio

# Connect OUT pin of vibration sensor to GPIO12
vibration_pin = Pin(12, Pin.IN)

async def run_server():
    while True:
        if vibration_pin.value():
            print("Vibration detected!",vibration_pin.value())
        else:
            print(".no vibration",vibration_pin.value())
        await asyncio.sleep(0.1)
         
async def main():
    await run_server()


asyncio.run(main())