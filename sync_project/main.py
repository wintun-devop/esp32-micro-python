import network
from machine import Pin
from time import sleep

# WiFi credentials
ssid = 'YOUR_SSID'
password = 'YOUR_PASS'

# Connect to WiFi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while not station.isconnected():
    pass
print('Connection successful')


led = Pin(2, Pin.OUT)
def main():
    while True:
        led.value(1) # led ON
        print("LED ON")
        sleep(0.5)
        led.value(0) # led OFF
        print("LED OFF")
        print("stat",station)
        print("stat",station.ifconfig())
        sleep(0.5)

if __name__ == "__main__":
    main()
