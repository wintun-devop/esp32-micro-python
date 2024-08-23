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
esptool --chip esp32 --port COM5 erase_flash
```
## Write MicroPython to wemos d1 flush
```
esptool --chip esp32 --port COM5 write_flash -z 0x1000 ESP32_GENERIC-20240602-v1.23.0.bin
```