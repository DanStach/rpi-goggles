Install Guide 
- install raspbain on rpi
  - us keyboard
  - wifi
- change interal settings
  - turn on camera port
  - turn on SSH
  - install specaial code for smaller display
  - turn off UI (maybe)
- download repo
  - open terminal
  - sudo mkdir /code
  - git clone https://github.com/DanStach/rpi-goggles
- setup to run python code on startup
  - https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/
  - sudo python3 /code/rpi-goggles/nightvisiongoggles.py &
- extra steps
  - rotate hdmi screen via software (180)
    - `sudo nano /boot/config.txt`
    - add following to last line of file
    - `lcd_rotate = 2`
    - exit and save <cntr + x> --> Y --> <enter>
  - set hdmi screeen resolution via software
    - https://learn.adafruit.com/adafruit-5-800x480-tft-hdmi-monitor-touchscreen-backpack/raspberry-pi-config
    - `sudo nano /boot/config.txt`
    - add following code to the file (middle of file)
      ```
      # uncomment if hdmi display is not detected and composite is being output
      hdmi_force_hotplug=1
      # uncomment to force a specific HDMI mode (here we are forcing 800x480!)
      hdmi_group=2
      hdmi_mode=87
      hdmi_cvt=800 480 60 6 0 0 0
      hdmi_drive=1
      ```
    - exit and save <cntr + x> --> Y --> <enter>


Todo: 
- create training video on software setup
- create training video hardware setup
- create demo video on final design
