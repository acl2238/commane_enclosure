# General

import time
import os
from datetime import datetime
import serial

# Changes current working directory to the Micro SD Card (or wherever you want really)
# I'm sure there's a better way to do it but this value is hardcoded for now
destination = '/media/acl2238/3332-6631' # This is the specific path to the specific MSD on this raspb
# To change destination, change this string to the filepath to any drive/directory
os.chdir(destination)

# GPS reader, unsure if which port matters
gps = open('/dev/ttyACM0')

# Will output file (can change this later)
now = datetime.now()
# Sets date and time in YYYY/MM/DD/TIME format
date_and_time = now.strftime("%F_%H%M")
# Output filename will always reflect the time the program was initially started
outputfilename = "gas_%s.csv" % date_and_time
output = open(outputfilename, "a")
if os.stat(outputfilename).st_size == 0: # If the output is empty, initial line with labels will be written
    output.write("Date, Time, Lattitude, Longitude, CO2 Value\n")
output.close() # Closes output for now, each iteration of a drawn line will open it again

currline = "" # Buffer

ser = serial.Serial("/dev/ttyS0", baudrate=9600, timeout = .5)
print("AN-137 RP3 to K-30")
ser.flushInput()
time.sleep(1)
linecounter = 0

# Whie loop
while True: 
    for line in gps: 
        '''RMC line contains time in GMT, 
        lattitude, longitude, and date in
        DD/MM/YYYY format'''
        if "RMC" in line:
            if linecounter == 60:
                quit()
            output = open(outputfilename, "a")

            ser.write(b'\xFE\x44\x00\x08\x02\x9F\x25')
            resp = ser.read(7)
            high = resp[3]
            low = resp[4]
            co2 = (high*256) + low

            split = line.split(',')
            date = split[9] 
            time = split[1]
            lat = split[3]
            latsign = split[4]
            long = split[5]
            longsign = split[6]
            carbon_dioxide_value = str(co2) 

            currline = "%s, %s, %s %s , %s %s , %s\n" % (date, time, lat, latsign, long, longsign, carbon_dioxide_value)

            output.write(currline) # Writes line by line to the results.csv file
            # Debugging, will print each line to terminal before the output gets closed
            print(currline)
            output.close() # Closes the output 
            linecounter+=1
