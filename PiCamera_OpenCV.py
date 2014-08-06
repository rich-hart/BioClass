import time
import picamera
import picamera.array

import cv2.cv as cv



with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        camera.resolution = (1024, 768)
        #camera.start_preview()
        
        #time.sleep(2)
        #camera.capture(stream, 'rgb')
        cv.NamedWindow("camera", 1)

        #capture = cv.CaptureFromCAM(0)

    while True:
        #img = cv.QueryFrame(capture)
        stream=cv.fromarray(stream)
        cv.ShowImage("camera", stream)
        if cv.WaitKey(10) == 27: #'Esc' Key 
            break
        #cv.DestroyAllWindows()
        #print(stream.array.shape)