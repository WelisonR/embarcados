# requires RPi_I2C_driver.py
import RPi_I2C_driver
from time import *
import smbus2
import bme280

mylcd = RPi_I2C_driver.lcd()

# bme280 device settings
i2c_port = 1
address = 0x76 
bus = smbus2.SMBus(i2c_port)
bme280_parameters = bme280.load_calibration_params(bus, address)

while True:
    # bme280 sensor data
    data = bme280.sample(bus, address, bme280_parameters)

    temperature  = round(data.temperature, 2)
    humidity = round(data.humidity, 2)
    pressure = round(data.pressure, 2)
    
    print(f"Temperatura: {temperature:.2f} °C")
    print(f"Umidade: {humidity:.2f} %")
    print(f"Pressão atmosférica: {pressure:.2f} hPa", end="\n\n")

    tempereture_humidity_str = f"T {temperature:.2f} U {humidity:.2f}"
    pressure_str = f"P {pressure:.2f}"

    # Display data in 2x16 LCD
    mylcd.lcd_display_string(tempereture_humidity_str, 1)
    mylcd.lcd_display_string(pressure_str, 2)

    sleep(1)
