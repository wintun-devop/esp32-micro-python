# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import machine
import uasyncio as asyncio

async def run_server():
     while True:
         print("running server!")
         await asyncio.sleep(5)
         
async def main():
    await run_server()


asyncio.run(main())