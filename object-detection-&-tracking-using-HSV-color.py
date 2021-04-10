import cv2
import numpy as np

def nothing(x):
    pass

#Creating UI for trackbar
cv2.namedWindow("Object Detection Result")
#creating the trackbar
cv2.createTrackbar("LH", "Object Detection Result", 0, 255, nothing)
cv2.createTrackbar("LS", "Object Detection Result", 0, 255, nothing)
cv2.createTrackbar("LV", "Object Detection Result", 0, 255, nothing)

cv2.createTrackbar("UH", "Object Detection Result", 255, 255, nothing)
cv2.createTrackbar("US", "Object Detection Result", 255, 255, nothing)
cv2.createTrackbar("UV", "Object Detection Result", 255, 255, nothing)

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
    lowerHue= cv2.getTrackbarPos("LH", "Object Detection Result")
    lowerSaturation= cv2.getTrackbarPos("LS", "Object Detection Result")
    lowerValue= cv2.getTrackbarPos("LV", "Object Detection Result")

    upperHue= cv2.getTrackbarPos("UH", "Object Detection Result")
    upperSaturation= cv2.getTrackbarPos("US", "Object Detection Result")
    upperValue= cv2.getTrackbarPos("UV", "Object Detection Result")

    #Set the upper and lower value
    getLowerValueBlue = np.array([lowerHue, lowerSaturation, lowerValue])
    getUpperValueBlue = np.array([upperHue, upperSaturation, upperValue])

    #set masking so only get the color between upper and lower value
    masking = cv2.inRange(hsv, getLowerValueBlue, getUpperValueBlue)

    #Use bitwise_and method to mask original image
    result = cv2.bitwise_and(frame, frame, mask=masking)

    cv2.imshow('Object Detection Result', result)

    key=cv2.waitKey(1) # esc key
    if key ==27:
        break

#Release the camera
capture.release()

cv2.destroyAllWindows()