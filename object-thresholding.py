import cv2 as cv
import numpy as np

img = cv.imread('dance.jpg', 0)

#if pixel value less than 127, will be assign into 0. 
#if pixel value greater than 127, will be assign into 255
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

#if the pixel value up to 127, will be the same as default color
#the rest will be remain 127
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)

#if pixel value is leff than 127, will be assign to 0
#the rest will be the same as default color
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)


cv.imshow('Image', img)
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)


cv.waitKey(0)
cv.destroyAllWindows()