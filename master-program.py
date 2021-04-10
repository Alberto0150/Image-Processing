import cv2
import numpy as np

def nothing(x):
    pass

#Creating UI Window for trackbar
cv2.namedWindow("Trackbar Window")
#Creating the trackbar
cv2.createTrackbar("LH", "Trackbar Window", 0, 360, nothing)
cv2.createTrackbar("LS", "Trackbar Window", 0, 255, nothing)
cv2.createTrackbar("LV", "Trackbar Window", 0, 255, nothing)

cv2.createTrackbar("UH", "Trackbar Window", 360, 360, nothing)
cv2.createTrackbar("US", "Trackbar Window", 255, 255, nothing)
cv2.createTrackbar("UV", "Trackbar Window", 255, 255, nothing)

#Capturing video
capture = cv2.VideoCapture(0)


while True:

    #Read video
    _, frame = capture.read() 

    #Set for threshold video
    _, framethr = capture.read()

    #Changing image into HSV color
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Get trackbar position
    lowerHue= cv2.getTrackbarPos("LH", "Trackbar Window")
    lowerSaturation= cv2.getTrackbarPos("LS", "Trackbar Window")
    lowerValue= cv2.getTrackbarPos("LV", "Trackbar Window")

    upperHue= cv2.getTrackbarPos("UH", "Trackbar Window")
    upperSaturation= cv2.getTrackbarPos("US", "Trackbar Window")
    upperValue= cv2.getTrackbarPos("UV", "Trackbar Window")

    #Set the upper and lower value
    getLowerValue = np.array([lowerHue, lowerSaturation, lowerValue])
    getUpperValue = np.array([upperHue, upperSaturation, upperValue])

    #Set masking so only get the color between upper and lower value
    masking = cv2.inRange(hsv, getLowerValue, getUpperValue)

    #Use bitwise_and method to mask original image
    resultmask = cv2.bitwise_and(frame, frame, mask=masking)

    #Apply threshold
    #Refference  https://stackoverflow.com/a/16887548/15296238
    framethr[(resultmask[...,1]<180)]=0

    cv2.imshow('thresholded', framethr)
    cv2.imshow('camera', resultmask)


    key=cv2.waitKey(1) # esc key
    if key ==27:
        break

#Release the camera
capture.release()

cv2.destroyAllWindows()