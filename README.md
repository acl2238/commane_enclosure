Please Read!!!

Parts List:

- CM-0111 vacuum pump
- Lithium Ion Battery (or any other modular power source, adapt as necessary)
- 12v to 5v converter
- Raspberry Pi 4 and Canakit Case
- Alphasense CO-B4 Carbon Monoxide Sensor
- K30 CO2 Sensor
- Adafruit ADS1115 A to D converter
- Generic USB GPS (Vfan)
- Enclosure Parts (see 3d files)
- 4.7 wide by 4.3 long push inserts
- M3 screws
- 2 Switches

Note 1: The main file is gas.py, K30 only tracks CO2

For Nick Frearson's reference

Instructions:

To run the data collection program at startup on newer models (likely including the one you are using:
1. Open terminal
2. Type "nano ~/.config/wayfire.ini"
3. Input these lines at the end of the file:

[autostart]

run = lxterminal -e python3 (path to script)

The path to script will look something like /home/name/.../k30.py

4. Make sure that all requirements are satisfied (refer to requirements.txt)
  - Note 2: Make sure Adafruit packages are installed following instructions on their website (blinka)
  - Note 3: If error message pops up saying failed to add edge detection, do this:

pip uninstall rpi.GPIO

pip install rpi-lgpio
5. Make sure all hardware is plugged in (batteries plugged in, GPS plugged into USB, pump on, etc)
  Note 4: Make sure that the Pi and pump are receiving 5v, the Alphasense CO sensor is receiving 3.3v (off a GPIO pin preferably) and the K30 is receiving 12v (from power source likely)
6. Edit the destination file in k30.py to point to whatever directory you want to save data to (I recommend making a folder in the code directory for storing all data)
7. reboot

The program will run continuously in a loop, and turning the switch to an "on" position will start logging today. Turning the switch to the "off" position will stop the dataogging and the program will wait for the next switch pull to start logging data again. Ideally the switch should be mounted to something and states labeled. 

<img width="482" alt="image" src="https://github.com/user-attachments/assets/35102166-ab32-47a1-b9ce-4e827ccf0fdc">

<img width="482" alt="image" src="https://github.com/user-attachments/assets/653c0e03-0f83-4532-a185-423f6711324d">

<img width="482" alt="image" src="https://github.com/user-attachments/assets/bbe5e317-d84b-4ec7-8f99-8cd6e810896d">

<img width="732" alt="image" src="https://github.com/user-attachments/assets/4c7ebf05-4fca-45c7-b6d9-a5096962b255">




