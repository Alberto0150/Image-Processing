import cv2
#read image
img = cv2.imread('dance.jpg', 0)
#print(img)

destroy = cv2.destroyAllWindows()

#showing image
img2 =cv2.imshow('fileImage', img)
# <fileImage> is the window name as the image is open
img2

# mask for 64-bit machine
getKey = cv2.waitKey(0) & 0xFF

if getKey == 27: # press esc to quit
    destroy
elif getKey == ord('s'):
    #write image into a file
    img3 = cv2.imwrite('newcopy.jpg',img)
    img3
    destroy