# visualizing temperatures and signalizing a breach
import machine
import utime

sensor_temp = machine.ADC(4)
led_onboard = machine.Pin(25, machine.Pin.OUT)

conversion_factor = 3.3 / (65535)

threshold = 28
def formatBar(num):
    return "|" * round(num)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721
    print(formatBar(temperature) + " " + str(temperature))
    if temperature > threshold:
        led_onboard.value(1)
        utime.sleep(1)
        led_onboard.value(0)
    utime.sleep(2)
 
