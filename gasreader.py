# Alphasense's shitty CO sensors don't work, this code is currently non-functional

# General

import time
import os
from datetime import datetime

# For the ADS board

import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA) # I2C interface
ads = ADS.ADS1115(i2c) # ADS

carbon_monoxide_input = AnalogIn(ads, ADS.P0, ADS.P1) # Carbon Monoxide Differential Input
# carbon_dioxide_input = AnalogIn(ads, ADS.CHANGETHIS # Carbon Dioxide Input

# Changes current working directory to the Micro SD Card (or wherever you want really)
# I'm sure there's a better way to do it but this value is hardcoded for now
destination = '/media/acl2238/3332-6631' # This is the specific path to the specific MSD on this raspb
# To change destination, change this string to the filepath to any drive/directory
os.chdir(destination)

# GPS reader, unsure if which port matters
gps = open('/dev/ttyACM0')

# Will create an output file titled with date in csv format (can change this later)
now = datetime.now()
# Sets date and time in YYYY/MM/DD/TIME format
date_and_time = now.strftime("%F_%H%M")
# Output filename will always reflect the time the program was initially started
outputfilename = "gas_%s.csv" % date_and_time
output = open(outputfilename, "a")
if os.stat(outputfilename).st_size == 0: # If the output is empty, initial line with labels will be written
    output.write("Date, Time, Lattitude, Longitude, CO Voltage, CO Value\n")
output.close() # Closes output for now, each iteration of a drawn line will open it again

currline = "" # Buffer

linecounter = 0

# Whie loop
while True: 
    for line in gps: 
        '''RMC line contains time in GMT, 
        lattitude, longitude, and date in
        DD/MM/YYYY format'''
        if "RMC" in line:
            if linecounter == 200:
                quit()
            output = open(outputfilename, "a")

            split = line.split(',')
            date = split[9] 
            time = split[1]
            lat = split[3]
            latsign = split[4]
            long = split[5]
            longsign = split[6]
            carbon_monoxide_voltage = carbon_monoxide_input.voltage
            carbon_monoxide_value = carbon_monoxide_input.value
            # carbon_dioxide = carbon_dioxide_input.voltage

            currline = "%s, %s, %s %s , %s %s , %s, %s\n" % (date, time, lat, latsign, long, longsign, carbon_monoxide_voltage, carbon_monoxide_value)

            output.write(currline) # Writes line by line to the results.csv file
            # Debugging, will print each line to terminal before the output gets closed
            print(currline)
            output.close() # Closes the output 
            linecounter+=1
