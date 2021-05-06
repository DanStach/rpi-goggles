from time import sleep
from signal import pause
import picamera

camera = picamera.PiCamera()
camera.led = False
camera.coloreffects = (128,0) # (128,0) creates a blk and green night vision effect


camera.start_preview()
pause()

