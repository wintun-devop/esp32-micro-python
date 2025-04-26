import machine
from machine import Pin,I2C
from time import sleep

#build in led for operation status
led = Pin(2, Pin.OUT)
#Digital output on GPIO15
do_pin = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

def main():
    while True:
        gas_detected = do_pin.value()
        #led on
        led.value(1)
        print("value",gas_detected)
        print("pin",do_pin)
        if gas_detected:
            print("⚠ High gas concentration detected!")
        else:
            print("✅ Air quality is normal.")
        #led off
        led.value(0)
        sleep(2)

if __name__ == "__main__":
    main()