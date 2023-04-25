# signalizing 2-digit temperatures by using the onboard LED
from machine import Pin, ADC
from utime import sleep

sensor_temp = ADC(4)
led_onboard = Pin(25, Pin.OUT)
conversion_factor = 3.3 / (65535)

while True:
    voltage = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (voltage - 0.706) / 0.001721
    print("V = " + str(voltage) + "    T = " + str(temperature))
    digits = []    # extracting digits
    tens = abs(int(temperature / 10))
    digits.append(tens)
    ones = abs(round(temperature) - tens * 10)
    digits.append(ones)
    sleep(6)
    for n in digits:    # blinking every digit
        sleep(3)
        for i in range(n):
            led_onboard.value(1)
            sleep(1)
            led_onboard.value(0)
            sleep(1)