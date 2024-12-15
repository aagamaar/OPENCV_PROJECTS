#importing the opencv and numpy packages
import cv2
import numpy as np

#Original image
img = cv2.imread("Resources_/ghostly-train.jpeg")
print(img.shape)

#Resized image
imgResize = cv2.resize(img,(1000,700))
print(imgResize.shape)

#To display the original and the resized image
cv2.imshow("Image",img)
cv2.imshow("Image Resized",imgResize)

cv2.waitKey(0)
