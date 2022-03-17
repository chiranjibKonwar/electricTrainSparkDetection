import cv2
import os
import glob
import time

imdir = '/home/chiranjib/Desktop/project_railway/1_video_live_streaming/'
ext = ['png', 'jpg', 'mp4']    # Add image formats here

files = []
[files.extend(glob.glob(imdir + '*.mp4'))]

caps = [cv2.VideoCapture(file) for file in files]



# Detecting multiple bright spots in an image with Python and OpenCV
# load the image, convert it to grayscale, and blur it


#from webcam we have to save mp4 videos of 1 second duration as sparks.mp4
for cap in caps:
    count = 1
    path = '/home/chiranjib/Desktop/project_railway/2_frames_from_video'
    while cap.isOpened():
        ret,frame = cap.read()
        if ret:
            cv2. imwrite(os. path. join(path , time.strftime("%Y-%m-%d:%H-%M-%S") +"_%d" % count +".jpg"), frame)
       	    count = count + 1
        if not ret:
            break

    cap.release()
    cv2.destroyAllWindows()

print("done!")


