#### Bioe 421/521, Jordan Miller, jmil@rice.edu ###
#### requires picamera and raspberry pi camera ####
# adapted from: http://www.raspberrypi.org/picamera-pure-python-interface-for-camera-module/

import picamera
#from time import sleep
import cv2.cv as cv
import time

camera = picamera.PiCamera()
camera.start_preview()

for i in range(100):
 camera.brightness = i
 sleep(0.1)

sleep(15)

#camera.capture('image.jpg')


#camera.vflip = True
#camera.hflip = True
#camera.brightness = 60

#camera.start_recording('video.h264')
#sleep(5)
#camera.stop_recording()

