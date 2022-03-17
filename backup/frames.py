import cv2
import os
import glob


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help="path to the video file")
args = vars(ap.parse_args())

# Detecting multiple bright spots in an image with Python and OpenCV
# load the image, convert it to grayscale, and blur it


#from webcam we have to save mp4 videos of 1 second duration as sparks.mp4
cap = cv2.VideoCapture(args["video"])
count = 1
path = '/home/chiranjib/Desktop/project_railway/2_frames_from_video'
while cap.isOpened():
    ret,frame = cap.read()
    if ret:
        cv2. imwrite(os. path. join(path , "frame%d.jpg" % count), frame)
       	count = count + 1
    if not ret:
        break

cap.release()
cv2.destroyAllWindows()




imdir = '/home/chiranjib/Desktop/project_railway/2_frames_from_video/'
ext = ['png', 'jpg', 'gif']    # Add image formats here

files = []
[files.extend(glob.glob(imdir + '*.jpg'))]

images = [cv2.imread(file) for file in files]

count = 1
path = "/home/chiranjib/Desktop/project_railway/4_frames_with_circle"
for image in images:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)

    #Detecting Circles in Images using OpenCV
    # detect circles in the image
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1.2, 100)
    # ensure at least some circles were found
    x=None
    if type(circles) != type(x):
        cv2.imwrite(os.path.join(path , 'frameWithCircle%d.jpg' % count), blurred)
        count += 1

print("done!")


