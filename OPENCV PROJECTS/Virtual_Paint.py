import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)  # Use 0 for default camera, 1 for secondary camera
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)  # Adjust brightness as needed

myColors =[[113,75,109,152,255,255],
           [17,54,156,40,140,255]]

myColorValues = [[255,0,0],
                 [0,255,255]]
#WE ARE WRITING IN THE ORDER OF BGR AND NOT RGB

myPoints = []  # [x, y, colorId]


def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)  # Might return 0, 0 if no contour found

        # Check if a contour was found before drawing a circle
        if x != 0 and y != 0:
            cv2.circle(imgResult, (x, y), 15, myColorValues[count], cv2.FILLED)
            newPoints.append([x, y, count])
        count += 1

    return newPoints


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    if len(contours) > 0:  # Check if there are any contours before iterating
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 500:  # Adjust area threshold as needed
                peri = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
                x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y


def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    if not success:  # Check for successful frame reading
        print("Error reading frame from camera")
        break

    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)

    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()