import cv2

# index 0 default device camera, if didn't detect, use -1
# replace with '<videoname.ext>' to use video
capture = cv2.VideoCapture(0) 

# saving the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# replace <outputVideo.avi> with custom file name and extension
# 20.0 is the FPS for the output, (640,480) is the default value for the resolution
saving = cv2.VideoWriter('outputVideo.avi', fourcc, 20.0,(640,480))

# isOpened() is case the video path or index false
while (capture.isOpened()):
    ret, frame =capture.read()
    if ret == True:

        #saving default color video
        saving.write(frame)

        #changing color to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('video', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'): #press 'q' to quit
            break
    else:
        break

capture.release()
saving.release()
cv2.destroyAllWindows()