# signalizing 2-digit temperatures by using the onboard LED
import machine
import utime

sensor_temp = machine.ADC(4)
led_onboard = machine.Pin(25, machine.Pin.OUT)

conversion_factor = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721
    print(temperature)
    digits = []    # extracting digits
    tens = abs(int(temperature / 10))
    digits.append(tens)
    ones = abs(round(temperature) - tens * 10)
    digits.append(ones)
    utime.sleep(6)
    for x in digits:    # blinking every digit
        utime.sleep(3)
        for i in range(x):
            led_onboard.value(1)
            utime.sleep(1)
            led_onboard.value(0)
            utime.sleep(1)
      