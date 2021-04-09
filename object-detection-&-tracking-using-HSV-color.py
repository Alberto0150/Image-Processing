import cv2
import numpy as np

def nothing(x):
    pass

#Creating UI for trackbar
cv2.namedWindow("Tracking")
#creating the trackbar
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)

cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

#Capturing video
capture = cv2.VideoCapture(0)


while True:
    #Read image
    #frame = cv2.imread('dance.jpg')

    #Read video
    _, frame = capture.read() 

    #Changing image into HSV color
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Get trackbar position
    lowerHue= cv2.getTrackbarPos("LH", "Tracking")
    lowerSaturation= cv2.getTrackbarPos("LS", "Tracking")
    lowerValue= cv2.getTrackbarPos("LV", "Tracking")

    upperHue= cv2.getTrackbarPos("UH", "Tracking")
    upperSaturation= cv2.getTrackbarPos("US", "Tracking")
    upperValue= cv2.getTrackbarPos("UV", "Tracking")

    #Set the upper and lower value
    getLowerValueBlue = np.array([lowerHue, lowerSaturation, lowerValue])
    getUpperValueBlue = np.array([upperHue, upperSaturation, upperValue])

    #set masking so only get the color between upper and lower value
    masking = cv2.inRange(hsv, getLowerValueBlue, getUpperValueBlue)

    #Use bitwise_and method to mask original image
    result = cv2.bitwise_and(frame, frame, mask=masking)

    cv2.imshow('result frame', result)

    key=cv2.waitKey(1) # esc key
    if key ==27:
        break

#Release the camera
capture.release()

cv2.destroyAllWindows()