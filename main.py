from machine import Pin
import time

led = Pin(25, Pin.OUT)
cycle = 0

while True:
    led.toggle()
    print("Blinking led... {}".format(cycle))
    cycle += 1
    time.sleep(2.0)
