import cv2
print("Package is imported ")

#FOR IMAGE

img = cv2.imread('Resources_/woman1.jpeg')
cv2.imshow("Output", img)
cv2.waitKey(0)

#FOR VIDEO

cap = cv2.VideoCapture("Resources_/6394054-uhd_4096_2048_24fps.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

#FOR WEBCAM

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, imf = cap.read()
    cv2.imshow("Video", imf)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break





