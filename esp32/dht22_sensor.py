import machine
import dht
import uasyncio as asyncio

sensor_pin = machine.Pin(4) 
sensor = dht.DHT22(sensor_pin)

async def read_sensor():
    while True:
        for attempt in range(3):
            try:
                sensor.measure()
                temp = sensor.temperature()
                humidity = sensor.humidity()
                print(f"Temperature: {temp}°C | Humidity: {humidity}%")
                break
            except OSError as e:
                print(f"Attempt {attempt+1}: Sensor Error", e)
                await asyncio.sleep(1)
        await asyncio.sleep(5)


async def main():
    await read_sensor()


asyncio.run(main())
