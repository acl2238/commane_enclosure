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
  - Note: Make sure Adafruit packages are installed following instructions on their website (blinka)
  - Note 2: If error message pops up saying failed to add edge detection, do this:

pip uninstall rpi.GPIO

pip install rpi-lgpio
5. Make sure all hardware is plugged in (batteries plugged in, GPS plugged into USB, pump on, etc)
6. Edit the destination file in k30.py to point to whatever directory you want to save data to (I recommend making a folder in the code directory for storing all data)
7. reboot

The program will run continuously in a loop, and turning the switch to an "on" position will start logging today. Turning the switch to the "off" position will stop the dataogging and the program will wait for the next switch pull to start logging data again. Ideally the switch should be mounted to something and states labeled. 
