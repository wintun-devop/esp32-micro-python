import machine
import dht
import os
import ubinascii
import network
import uasyncio as asyncio
from umqtt.robust import MQTTClient




# WiFi credentials
ssid = 'your network'
password = 'your password'

# Connect to WiFi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while not station.isconnected():
    pass
print('Connection successful')

# --- MQTT Setup ---
IOT_ENDPOINT = b'your_end_point'
CLIENT_ID = b'ufakflasf'
TOPIC = b'room/data'
cert = """
-----BEGIN CERTIFICATE-----
MyJ6DV3FXk1jxR6l5/
q8z/RHusy+CSYe12/a9DXpPq9Dd39vYiicgF90nRN/ozrCl2W4np43njLYWHARjG
Dvp1fVdy9eKFvCJrYNV5pSk7mq390viIeHqQrkCW3Edw67aSi5AZ85J9mlwREWHU
hIzjT4vDuhPnb7fdEM1GOIEro/uXaNfYS9vES9VjtiYnM5fPqXubHd0VY7Vg
-----END CERTIFICATE-----
"""
key = """
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAklrwrAaZA6GhhmyYKKswqUGshSkiGkKJ0MMGEhGGmduLmOjz
vd1WC4S
kLbJXkVy+YB22hE8+Ut2qZ9hKr3dRLO1ePkEnleiMwGYz+oQpyJwJqtZEuRC7a2c
MEoCwthaOKaMUph
/3HHRJVid6xGX4kGLP0QdQ8WVqM/8eL5p6NRsov1CPEWsQGW4e8SMY6Vu72sClIk
G6xjJKp/UYwl7M0o/plw1zrGUi3wQai3pzQT1I/OSrJ1RieC8BM=
-----END RSA PRIVATE KEY-----
"""
ca_certs="""-----BEGIN CERTIFICATE-----
MIIDQTCCAimgAwIBAgITBmyfz5m/jAo54vB4ikPmljZbyjANBgkqhkiG9w0BAQsF
ADA5MQswCQYDVQQGEwJVUzEPMA0GA1UEChMGQW1hem9uMRkwFwYDVQQDExBBbWF6
b24gUm9vdCBDQSAxMB4XDTE1MDUyNjAwMDAwMFoXDTM4MDExNzAwMDAwMFowOTEL
M
o/ufQJVtMVT8QtPHRh8jrdkPSHCa2XV4cdFyQzR1bldZwgJcJmApzyMZFo6IQ6XU
5MsI+yMRQ+hDKXJioaldXgjUkK642M4UwtBV8ob2xJNDd2ZhwLnoQdeXeGADbkpy
rqXRfboQnoZsG4q5WTP468SQvvG5
-----END CERTIFICATE-----"""

mqtt_params = {
    'server': IOT_ENDPOINT,
    'port': 8883,
    'ssl': True,
    'ssl_params': {
        'cert': cert,
        'key': key,
       # 'ca_certs':ca_certs
    }
}

client = MQTTClient(client_id=CLIENT_ID, **mqtt_params)
client.connect()
print('MQTT connected')

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
