import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dance.jpg',0)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

#kernel is a shape which applied to image
#(2,2) is a square shape
#iteration is how much time it applied
kernal = np.ones((2,2), np.uint8)
dilation = cv2.dilate(mask, kernal, iterations=2)
erosion = cv2.erode(mask, kernal, iterations=2)

#define titles for showing
titles = ['image', 'mask', 'dilation', 'erosion']
#pass the image frame value
images = [img, mask, dilation, erosion]

for i in range(4):
    #plt.subplot have 3 argument
    #1st argument define row, 2nd argument define column
    #3rd argument index of image
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    
    plt.title(titles[i])
    #hide the tick value of x ,y bar coordinate
    plt.xticks([]),plt.yticks([])

plt.show()