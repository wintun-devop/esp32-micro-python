import machine
from machine import Pin,I2C

#build in led for operation status
led = Pin(2, Pin.OUT)

def main():
    # ESP32 has GPIO0 to GPIO39 
    for i in range(30):
        try:
            pin = machine.Pin(i)
            # led ON
            led.value(1) 
            adc = machine.ADC(machine.Pin(i))
            pwm = machine.PWM(machine.Pin(i))
            touch = machine.TouchPad(machine.Pin(i))
            print(f"GPIO{i} is available")
            print(f"adc:{adc}-pwm:{pwm}-touch:{touch}")
            led.value(0) 
        except:
            pass


if __name__ == "__main__":
    main()
