# rpi-goggles
Raspberry Pi night vision goggle code. python code that creates a side by side stero view (steroscopic) from a single camera
Install instruction can found in the [INSTALL.md](INSTALL.md)

## Hardware Ver1:
- RPi 3b+ 
- noir camera (arducam B003503)
  - Resolution: 5MP 2592×1944
  - Video: 1080p 30 fps, 720p 60fps, 480p 90fps
- desktop monitor HDMI (1600x900)

## Hardware Ver2:
- RPi 3b+
- noir camera (arducam B003503)
  - Resolution: 5MP 2592×1944
  - Video: 1080p 30 fps, 720p 60fps, 480p 90fps
- 3.5 Inch HDMI (UCTRONICS)(480*320)

## Hardware Ver3:
- RPi 0W
- noir camera (arducam B003503)
  - Resolution: 5MP 2592×1944
  - Video: 1080p 30 fps, 720p 60fps, 480p 90fps
-  7 Inch HDMI (MakerFocus)(800x480)

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
