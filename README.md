# rpi-goggles
Raspberry Pi night vision goggle code. python code that creates a side by side stero view (steroscopic) from a single camera

## Hardware: (very fast)
- RPi 3b+ (1-5% cpu usage)
- noir camera
- desktop monitor HDMI (1600x900)

## Notes:
- test: RPi 3b+ (1-5% cpu usage)
- test: RPi 0W (5-10% cpu usage)
- Display is HDMI (there seems to be lag issues when using Display Connector DSI, or GPIO)

## Reference
- orginal code found at https://www.raspberrypi.org/forums/viewtopic.php?t=187070
- other youtube link: https://www.youtube.com/watch?v=JdtEr_CbDv0

## usefull commands
- sudo python3 /code/rpi-goggles/nightvisiongoggles.py
- sudo raspivid -t 800000000
- stop command: sudo pkill -9 python
- stop command: sudo pkill -9 raspivid
