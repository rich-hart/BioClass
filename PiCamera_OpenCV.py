import io
import time
import picamera
import cv2
import numpy as np
import cv2.cv as cv
# Create the in-memory stream
stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    camera.capture(stream, format='jpeg')
# Construct a numpy array from the stream
data = np.fromstring(stream.getvalue(), dtype=np.uint8)
# "Decode" the image from the array, preserving colour
image = cv2.imdecode(data, 1)
# OpenCV returns an array with data in BGR order. If you want RGB instead
# use the following...
#image = image[:, :, ::-1]

cv.NamedWindow("camera", 1)

#capture = cv.CaptureFromCAM(0)

while True:
    #img = cv.QueryFrame(capture)
    
    cv.ShowImage("camera", cv.fromarray(image))
    if cv.WaitKey(10) == 27:
        break
cv.DestroyAllWindows()

