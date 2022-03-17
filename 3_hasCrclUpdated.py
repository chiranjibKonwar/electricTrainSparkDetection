import cv2
import os
import glob

imdir = '/home/chiranjib/Desktop/project_railway/3_circle_check/'
ext = ['png', 'jpg', 'gif']    # Add image formats here

# Detecting multiple bright spots in an image with Python and OpenCV
# load the image, convert it to grayscale, and blur it
count = 1
files = []
[files.extend(glob.glob(imdir + '*.jpg'))]

path = "/home/chiranjib/Desktop/project_railway/4_frames_with_circle/"
for file in files:
    filename = os.path.basename(file)
    image = cv2.imread(file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)

    #Detecting Circles in Images using OpenCV
    # detect circles in the image
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1.2, 100)
    # ensure at least some circles were found
    x=None
    if type(circles) != type(x):
        cv2.imwrite(os.path.join(path , filename), blurred)
        count += 1

print("done!")


