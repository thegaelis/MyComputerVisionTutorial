import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    #create a temp variable to draw a line
    #draw a line: cv2.line(image, startposition, endposition, color, thickness (-1 to fill))
    img = cv2.line(frame, (0,0), (255,255), (255,129,222), 10)
    #draw a rectangle: cv2.rectangle (image, centerposition, radius (width, length), color, thickness )
    img = cv2.rectangle(img, (128,128), (96,96), (255,0,0), -1)
    #draw a circle: cv2.circle (image, centerposition, radius (r), color, thickness)
    img = cv2.circle (img, (128,128), 16, (0,255,0), -1)
    #draw text:
    # - create font:
    font = cv2.FONT_HERSHEY_COMPLEX
    # - add text to live feed: cv2.putText(image, text content, center position, font, font scale, color, line thickness, line type)
    img = cv2.putText(img, 'Press \'q\' to exit', (255,100), font, 1, (0,0,255),1, cv2.LINE_AA)
    cv2.imshow('Live capture', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
