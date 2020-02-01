# rpi-goggles
Raspberry Pi night vision goggle code. python code that creates a side by side stero view (steroscopic) from a single camera

##Hardware: (very fast)
- RPi 3b+
- noir camera
- desktop monitor (1600x900)

##Reference
- orginal code found at https://www.raspberrypi.org/forums/viewtopic.php?t=187070
- other youtube link: https://www.youtube.com/watch?v=JdtEr_CbDv0

##usefull commands
- sudo python3 /code/rpi-goggles/nightvisiongoggles.py
- sudo raspivid -t 800000000
- stop command: sudo pkill -9 python
- stop command: sudo pkill -9 raspivid
