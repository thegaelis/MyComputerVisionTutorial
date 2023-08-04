#Import OpenCV library
import cv2

#Open an image: img = cv2.imread (directory, mode)
# Modes:
# - -1, cv2.IMREAD_COLOR
# - 0, cv2.IMREAD_GRAYSCALE
# - 1, cv2.IMREAD_UNCHANGED
img = cv2.imread('assets/demo.png', 0)

#To show a picture on a window : cv2.imshow (window name, image to show)
cv2.imshow('Image', img)
#Catch a key to close window 
# cv2.waitkey(0) -> wait any key to press for an infinite amount of time
# cv2.waitkey(x sec) -> wait any key up to x sec, if not, skip
# cv2.destroyAllWindows -> close windows if any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()