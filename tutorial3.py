#importing numpy for scientific calculation
import numpy as np
import cv2

#Video capture from webcam or video: cv2.VideoCapture(n)
#Webcam or video: n=0 or n=1 if there's a webcam
# n cams: n
#video: 'directory of video' ->cv2.VideoCapture('directory of video')
cap = cv2.VideoCapture(1)

#A loop to catch a key to stop recording
#ret: make sure that the capture would work properly
while True:
    ret, frame = cap.read()
    #Showing live capture
    cv2.imshow('Live capture',frame)
    #If the user press q, the live capture will stop
    if cv2.waitKey(1) == ord('q'):
        break

#Release the camera resource
cap.release()
#Shut down windows
cv2.destroyAllWindows()