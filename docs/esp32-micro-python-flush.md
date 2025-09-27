### Ref-1( https://micropython.org/download/ESP32_GENERIC/)
### Ref-2(https://medium.com/@andymule/micropython-on-esp32-e54998966e9)
### Ref-3(https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)
### Ref-4(https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads) - usb driver
## virtial environment set-up
```
python -m venv esp32-env
```
```
esp32-env/Script/activate
```
## installing necessary tools
```
pip install esptool
```
## Check the com port and erase flash(here my chip is esp8266)
```
esptool --chip esp32 --port COM3 erase-flash
```
## Write MicroPython to wemos d1 flush
```
esptool --chip esp32 --port COM3 write-flash -z 0x1000 ESP32_GENERIC-20250809-v1.26.0.bin
```

### Micropython IMU Site
```
https://github.com/micropython-IMU
```

###
```
esptool --port COM3 chip-id
```

### micro python command line interaction
```
pip install adafruit-ampy
```
- deliver file to micropython
```
ampy --port COMx put certificate.pem.crt
ampy --port COMx put private.pem.key
ampy --port COMx put AmazonRootCA1.pem
```

- deliver file to micropython with serial specific rate
```
ampy --port COMx put -b 115200 certificate.pem.crt
ampy --port COMx put -b 115200 private.pem.key
ampy --port COMx put -b 115200 AmazonRootCA1.pem
```

- delete file
```
ampy --port COMx rm certificate.pem.crt
ampy --port COMx rm private.pem.key
ampy --port COMx rm AmazonRootCA1.pem

```
- list file
```
ampy --port COMx ls
```