import cv2
import numpy as np

capture = cv2.VideoCapture(0)

ret, frame1 = capture.read()
ret, frame2 = capture.read()

while capture.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    # easier to find out contour in the latest stages
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    cv2.imshow("inter", frame1)

    if cv2.waitKey(40)==27:
        break

cv2.destroyAllWindows()
capture.release()