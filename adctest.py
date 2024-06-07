import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time

print("cp1")

i2c = busio.I2C(board.SCL, board.SDA)

print("cp2")

ads = ADS.ADS1115(i2c)

print("cp3")

while True:
    chan0 = AnalogIn(ads, ADS.P0) 
    chan1 = AnalogIn(ads, ADS.P1)
    combined = AnalogIn(ads, ADS.P0, ADS.P1)

    #chan2 = AnalogIn(ads, ADS.P2) 
    #chan3 = AnalogIn(ads, ADS.P3)

    time.sleep(3)

    print(chan0.value, chan0.voltage)
    print(chan1.value, chan1.voltage)
    print(combined.value, combined.voltage)

    #print(chan2.value, chan2.voltage)
    #print(chan3.value, chan3.voltage)


