import cv2
import numpy as np

img = cv2.imread("Resources_/woman2.jpeg")

width, height = 250, 350
pts1 = np.float32([[390,170],[1150,170],[335,430],[1180,430]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)






