import cv2
import numpy as np

def nothing(x):
    pass

while True:
    frame = cv2.imread('dance.jpg')

    #Changing image into HSV color
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Set the upper and lower value
    getLowerValueBlue = np.array([110, 50, 50])
    getUpperValueBlue = np.array([130, 255, 255])

    #set masking so only get the color between upper and lower value
    masking = cv2.inRange(hsv, getLowerValueBlue, getUpperValueBlue)

    #Use bitwise_and method to mask original image
    result = cv2.bitwise_and(frame, frame, mask=masking)

    cv2.imshow('result frame', result)

    key=cv2.waitKey(1)
    if key ==27:
        break

cv2.destroyAllWindows()