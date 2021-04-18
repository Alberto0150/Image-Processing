import cv2
import numpy as np

capture = cv2.VideoCapture('testvideo.avi')

ret, frame1 = capture.read()
ret, frame2 = capture.read()

while capture.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    # easier to find out contour in the latest stages
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    # blur the greyscale frame
    # (5,5) is the kernal size
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    # find out the threshold
    _, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)

    dilated = cv2.dilate(thresh, None, iterations=3)

    # find out the contour
    # SECOND ARGUMENT = MODE
    # THIRD ARGUMENT = METHOD
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)




    # outline object contours
    # apply the contours to original frame
    # THIRD ARGUMENT = CONTOUR ID -> -1 = apply all the contours
    # FORTH ARGUMENT = COLOR
    # FIFTH ARGUMENT = THICKNESS
    cv2.drawContours(frame1, contours, -1, (0,255,0), 2)


    cv2.imshow("feed", frame1)

    # assign value frame1 from frame2
    frame1=frame2

    #reading new frame in frame2
    ret, frame2 = capture.read()

    if cv2.waitKey(40)==27:
        break

cv2.destroyAllWindows()
capture.release()