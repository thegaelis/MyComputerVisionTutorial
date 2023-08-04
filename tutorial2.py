import cv2

#see how computer intepret and represent the picture.

img = cv2.imread('assets/demo.png')

#print the image value matrix
print(img)
#show how many rows, columns and channels in the picture
print(img.shape)

#the matrix of picture is a l x w matrix which contain color value.
#print first row of image matrix
print(img[0])


#change the value contain in the pixel in matrix

for i in range (100):
    for j in range(100):
        img[i][j]= [255,255,255] #RGB color [R,G,B], (255,255,255) -> white


#copy and paste part of an image
#copy the area from upper left to lower right
tag = img[500:700,600:900] 
#paste an image to an area from upper left to lower right
img[500:700, 600:900] = tag
#!IMPORTANT: The paste image must be appropriate

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('Image1',tag)
cv2.waitKey(0)
cv2.destroyAllWindows()



