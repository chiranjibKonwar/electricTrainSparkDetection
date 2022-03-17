# Detecting multiple bright spots in an image with Python and OpenCV
# import the necessary packages
from imutils import contours
from skimage import measure
import numpy as np
import argparse
import imutils
import cv2
import os
import glob


imdir = '/home/chiranjib/Desktop/project_railway/2_frames_from_video/'
ext = ['png', 'jpg', 'gif']    # Add image formats here

files = []
[files.extend(glob.glob(imdir + '*.jpg'))]

images = [cv2.imread(file) for file in files]

# Detecting multiple bright spots in an image with Python and OpenCV
# load the image, convert it to grayscale, and blur it
count = 1
for image in images:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)


    # Detecting multiple bright spots in an image with Python and OpenCV
    # threshold the image to reveal light regions in the
    # blurred image
    # Note how the bright areas of the image are now all white while the rest of the image is set to black.

    thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]

    # Detecting multiple bright spots in an image with Python and OpenCV
    # perform a series of erosions and dilations to remove
    # any small blobs of noise from the thresholded image
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=4)

    #Detecting multiple bright spots in an image with Python and OpenCV
    # perform a connected component analysis on the thresholded
    # image, then initialize a mask to store only the "large"
    # components
    labels = measure.label(thresh, connectivity=2, background=0)
    mask = np.zeros(thresh.shape, dtype="uint8")
    # loop over the unique components
    for label in np.unique(labels):
	# if this is the background label, ignore it
        if label == 0:
            continue
        # otherwise, construct the label mask and count the
        # number of pixels 
        labelMask = np.zeros(thresh.shape, dtype="uint8")
        labelMask[labels == label] = 255
        numPixels = cv2.countNonZero(labelMask)
        # if the number of pixels in the component is sufficiently
        # large, then add it to our mask of "large blobs"
        if numPixels > 300:
            mask = cv2.add(mask, labelMask)

        #Detecting multiple bright spots in an image with Python and OpenCV
        # find the contours in the mask, then sort them from left to
        # right
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    if len(cnts) > 0:
        cnts = contours.sort_contours(cnts)[0]
    # loop over the contours
        for (i, c) in enumerate(cnts):
            # draw the bright spot on the image
            (x, y, w, h) = cv2.boundingRect(c)
            ((cX, cY), radius) = cv2.minEnclosingCircle(c)
            cv2.circle(blurred, (int(cX), int(cY)), int(radius),
            (0, 0, 255), 3)
            cv2.putText(blurred, "#{}".format(i + 1), (x, y - 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
            # show the output image
        path = '/home/chiranjib/Desktop/project_railway/3_circle_check/'
        cv2.imwrite(os.path.join(path , 'circle_check%d.jpg' % count), blurred)
        count += 1
        print("Done!")










