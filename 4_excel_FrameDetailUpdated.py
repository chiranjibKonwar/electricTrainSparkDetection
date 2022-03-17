import os
import glob
import pandas as pd

imdir = '/home/chiranjib/Desktop/project_railway/4_frames_with_circle/'
ext = ['png', 'jpg', 'gif']    # Add image formats here

files = []
[files.extend(glob.glob(imdir + '*.jpg'))]


#writer = pd.ExcelWriter("filename_capturedDateTime_GPS_lat_long.xlsx", engine="xlsxwriter")
df = pd.DataFrame(columns=['date','time','frameID','GPS_latitude','GPS_longitude'])

for file in files:
    filename = os.path.basename(file)
    date = filename.split(":")[0]
    time = filename.split(":")[1].split("_")[0]
    frameID = filename.split(":")[1].split("_")[1].split(".")[0]
    df = df.append({'date' : date, 'time' : time, 'frameID' : frameID}, ignore_index = True)
    
print(df)
df.to_excel("frameID_capturedDateTime_GPS_lat_long.xlsx",
             sheet_name='imageDateTimeGPS')







