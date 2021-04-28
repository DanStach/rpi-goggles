from time import sleep
from signal import pause
import picamera

camera = picamera.PiCamera()
camera.led = False

camera.start_preview()
pause()

