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

# ADAPTIVE THRESHOLD
# 2 Type: .ADAPTIVE_THRESH_MEAN_C & .ADAPTIVE_THRESH_GAUSSIAN_C
# 255 is the maximum value to a pixel
# 11 is the block size, block size is the size of the neightbourhood area
# 2 is the C const value
th4 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)


cv.imshow('Image', img)
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)
cv.imshow('th4', th4)



cv.waitKey(0)
cv.destroyAllWindows()