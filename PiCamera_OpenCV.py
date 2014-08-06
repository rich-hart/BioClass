import io
import time
import picamera
import cv2
import numpy as np
import cv2.cv as cv
# Create the in-memory stream
stream = io.BytesIO()


cv.NamedWindow("camera", 1)

#capture = cv.CaptureFromCAM(0)
with picamera.PiCamera() as camera:
    with picamera.PiCamera() as camera:
        while True:
            #img = cv.QueryFrame(capture)
            camera.capture(stream, format='jpeg')
            data = np.fromstring(stream.getvalue(), dtype=np.uint8)
            image = cv2.imdecode(data, 1)
            cv.ShowImage("camera", cv.fromarray(image))
            if cv.WaitKey(10) == 27:
                break
cv.DestroyAllWindows()

