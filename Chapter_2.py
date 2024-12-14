import cv2
import numpy as np

#This is to read the colored image
img = cv2.imread("Resources_/woman2.jpeg")

#This is to read the colored image to gray image
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",imgGray)

#This is to read the colored image to blurred image
img_colored_to_blur = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("Colored Image To Blurred Image",img_colored_to_blur)

#This is to read the gray image to blurred image
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Blur Image",imgBlur)

#This is to convert the colored image to canny image
imgCanny = cv2.Canny(img,100,100)
cv2.imshow("Canny Image",imgCanny)

#Defining the kernel
kernel=np.ones( (5,5), np.uint8)

#This is to convert the canny image to dilation image
imgDilation = cv2.dilate(imgCanny, kernel, iterations = 1)
cv2.imshow("Dilated Image",imgDilation)

#This is to convert the dilation image to eroded image
imgEroded = cv2.erode(imgDilation ,kernel, iterations = 1)
cv2.imshow("Erode Image",imgEroded)


cv2.waitKey(0)