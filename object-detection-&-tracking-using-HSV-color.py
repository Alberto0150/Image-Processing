import cv2
import numpy as np

def nothing(x):
    pass

#Creating UI for trackbar
cv2.namedWindow("setting")
#creating the trackbar
cv2.createTrackbar("LH", "setting", 0, 255, nothing)
cv2.createTrackbar("LS", "setting", 0, 255, nothing)
cv2.createTrackbar("LV", "setting", 0, 255, nothing)

cv2.createTrackbar("UH", "setting", 255, 255, nothing)
cv2.createTrackbar("US", "setting", 255, 255, nothing)
cv2.createTrackbar("UV", "setting", 255, 255, nothing)

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
    lowerHue= cv2.getTrackbarPos("LH", "setting")
    lowerSaturation= cv2.getTrackbarPos("LS", "setting")
    lowerValue= cv2.getTrackbarPos("LV", "setting")

    upperHue= cv2.getTrackbarPos("UH", "setting")
    upperSaturation= cv2.getTrackbarPos("US", "setting")
    upperValue= cv2.getTrackbarPos("UV", "setting")

    #Set the upper and lower value
    getLowerValueBlue = np.array([lowerHue, lowerSaturation, lowerValue])
    getUpperValueBlue = np.array([upperHue, upperSaturation, upperValue])

    #set masking so only get the color between upper and lower value
    masking = cv2.inRange(hsv, getLowerValueBlue, getUpperValueBlue)

    #Use bitwise_and method to mask original image
    result = cv2.bitwise_and(frame, frame, mask=masking)

    cv2.imshow('Object Detection Result', result)

    key=cv2.waitKey(1) 
    if key ==27: # esc key
        break

#Release the camera
capture.release()

cv2.destroyAllWindows()