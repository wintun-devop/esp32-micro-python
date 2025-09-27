import network
import machine
import dht
import ubinascii
import uasyncio as asyncio
from umqtt.robust import MQTTClient

# — Wi-Fi —
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect('HomeUIOO', 'sfiasfkjasfl')
while not sta.isconnected():
    pass


#sensor pin
sensor_pin = machine.Pin(4) 
sensor = dht.DHT22(sensor_pin)

async def read_sensor():
    while True:
        for attempt in range(3):
            try:
                sensor.measure()
                temp = sensor.temperature()
                humidity = sensor.humidity()
                machine_id=get_machine_id()
                print('Wi-Fi:', sta.ifconfig())
                print(f"Machine:{machine_id} | Temperature: {temp}°C | Humidity: {humidity}%")
                break
            except OSError as e:
                print(f"Attempt {attempt+1}: Sensor Error", e)
                await asyncio.sleep(1)
        await asyncio.sleep(20)


async def main():
    await read_sensor()
    
def get_machine_id()->str:
    machine_id = str(ubinascii.hexlify(machine.unique_id()).decode())
    return machine_id


asyncio.run(main())