import io
import picamera
import cv2
import numpy as np
#saving the picture to an in-program stream rather than a file
stream = io.BytesIO()

#to speed things up, lower the resolution of the camera
CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240

with picamera.PiCamera() as camera:
    camera.resolution = (CAMERA_WIDTH, CAMERA_HEIGHT)
    #capture into stream
    camera.capture(stream, format='jpeg')
#convert image into numpy array
data = np.fromstring(stream.getvalue(), dtype=np.uint8)
#turn the array into a cv2 image
image = cv2.imdecode(data, 1)

#load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_alt.xml')

#convert to grayscale, which is easier
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#look for faces over the given image using the loaded cascade file
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    #opencv has built in image manipulation functions
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

#use opencv built in window to show the image
# leave out if your Raspberry Pi isn't set up to display windows
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
