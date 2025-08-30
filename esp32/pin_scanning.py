import uasyncio as asyncio
from machine import SoftI2C, Pin
import ssd1306
"""
# Use the working pin combo
#i2c = SoftI2C(scl=Pin(5), sda=Pin(21))
#i2c = SoftI2C(scl=Pin(5), sda=Pin(4))
#oled = ssd1306.SSD1306_I2C(128, 64, i2c)
#oled = ssd1306.SSD1306_I2C(128, 64, i2c)
led_pin =Pin(16, Pin.OUT)
led_pin.value(1)
sda_pins = [4, 21]
scl_pins = [5, 22]

async def run_server():
    while True:
        print("hello")
        for sda in sda_pins:
            for scl in scl_pins:
                try:
                    i2c = SoftI2C(scl=Pin(scl), sda=Pin(sda))
                    devices = i2c.scan()
                    print(f"SDA={sda}, SCL={scl} → {devices}")
                except Exception as e:
                    print(f"Error with SDA={sda}, SCL={scl}: {e}")
        #print("i2c",i2c)
        #print("oled",oled)
        #print("led_pin",led_pin)
        #print("Scan result:", i2c.scan())
        #oled.fill(0)
        #oled.text("Hello Win!", 0, 0)
        #oled.show()
        await asyncio.sleep(2)
"""
# Enable OLED power (common on TTGO boards)
led_pin = Pin(16, Pin.OUT)
led_pin.value(1)

# Candidate SDA/SCL pins to scan
sda_pins = [4, 21]
scl_pins = [5, 22]

# Track whether OLED was initialized
oled_initialized = False

async def run_server():
    global oled_initialized
    while True:
        print("🔍 Scanning I2C buses...")
        for sda in sda_pins:
            for scl in scl_pins:
                try:
                    i2c = SoftI2C(scl=Pin(scl), sda=Pin(sda))
                    devices = i2c.scan()
                    print(f"SDA={sda}, SCL={scl} → {devices}")

                    # Check for OLED address
                    if 60 in devices or 61 in devices:
                        print(f"✅ OLED likely found at SDA={sda}, SCL={scl}")
                        if not oled_initialized:
                            try:
                                oled = ssd1306.SSD1306_I2C(128, 64, i2c)
                                oled.fill(0)
                                oled.text("Hello Win!", 0, 0)
                                oled.show()
                                print("🎉 OLED initialized and message displayed.")
                                oled_initialized = True
                            except Exception as e:
                                print(f"⚠️ OLED init failed: {e}")
                except Exception as e:
                    print(f"❌ Error with SDA={sda}, SCL={scl}: {e}")
        await asyncio.sleep(5)

async def main():
    await run_server()

asyncio.run(main())