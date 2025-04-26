import machine,time,dht


# Define the pin where DHT11 is connected
# GPIO4
sensor_pin = machine.Pin(4) 
sensor = dht.DHT11(sensor_pin)

while True:
    try:
        sensor.measure()  # Get readings
        temp = sensor.temperature()  # Temperature in Celsius
        humidity = sensor.humidity()  # Humidity in %
        print(f"Temperature: {temp}°C | Humidity: {humidity}%")
        time.sleep(2)  # Wait for 2 seconds before reading again
    except OSError as e:
        print("Failed to read sensor!")
