from picamera import mmalobj as mo, mmal
from signal import pause

# define values from the camera window
#my desktop (pal) 720 x 576
camResW = 640
camResH = 480
camFramR = 30

# starting corner of your windows (upper-left position) 
cornerX = 1
cornerY = 1
windowSpacer = 5 # space between the 2 windows

camera = mo.MMALCamera()
splitter = mo.MMALSplitter()
render_l = mo.MMALRenderer()
render_r = mo.MMALRenderer()
# The 960 and 720 are the resolution.  This can be changed to fill your display properly.  I believe I'm using 960 and 1080 on mine.
camera.outputs[0].framesize = (camResW,camResH)
# This originally was 30, but then I the latency is too high and it's nearly impossible to navigate while wearing a head mounted display.
camera.outputs[0].framerate = camFramR
camera.outputs[0].commit()

p = render_l.inputs[0].params[mmal.MMAL_PARAMETER_DISPLAYREGION]
p.set = mmal.MMAL_DISPLAY_SET_FULLSCREEN | mmal.MMAL_DISPLAY_SET_DEST_RECT
p.fullscreen = False
# These parameters control the X,Y and scale of the left image showing up on your display
p.dest_rect = mmal.MMAL_RECT_T(cornerX, cornerY, camResW, camResH)
render_l.inputs[0].params[mmal.MMAL_PARAMETER_DISPLAYREGION] = p
# These control the X,Y and the scale of the right image showing up on your display.
p.dest_rect = mmal.MMAL_RECT_T(cornerX+windowSpacer+camResW, cornerY, camResW, camResH)
render_r.inputs[0].params[mmal.MMAL_PARAMETER_DISPLAYREGION] = p

splitter.connect(camera.outputs[0])
render_l.connect(splitter.outputs[0])
render_r.connect(splitter.outputs[1])

splitter.enable()
render_l.enable()
render_r.enable()

pause()
