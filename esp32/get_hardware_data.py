import time,sys,machine,ubinascii
from machine import Pin
from time import sleep



def main():
    while True:
        print("machine_id",get_machine_id())
        print("hardware_plaform",get_hardware_platform())
        print("current_time",get_current_time())
        sleep(1)


def get_machine_id()->str:
    machine_id = str(ubinascii.hexlify(machine.unique_id()).decode())
    return machine_id

def get_hardware_platform()->str:
    platform=str(sys.platform)
    return platform

def get_current_time()->str:
    year, month, day, hour, minute, second, weekday, yearday = time.gmtime()
    utc_time_str = "{:04}-{:02}-{:02}T{:02}:{:02}:{:02}Z".format(year, month, day, hour, minute, second)
    return utc_time_str

if __name__ == "__main__":
    main()
