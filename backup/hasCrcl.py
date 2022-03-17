import cv2
import argparse
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)

#Detecting Circles in Images using OpenCV
# detect circles in the image
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1.2, 100)
# ensure at least some circles were found
x=None
path = "/home/chiranjib/Desktop/project_railway/4_frames_with_circle"
if type(circles) != type(x):
    cv2.imwrite(os.path.join(path , 'frameWithCircle.jpg'), blurred)


