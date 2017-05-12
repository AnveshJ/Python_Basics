import cv2
import random
import sys
import os
import numpy as np
import math

from os import listdir
from os.path import isfile, join

#Appending_Path
sys.path.append("/Users/anveshjadon/Desktop/Python/task1")

#Declaring_Images_Arrays
images1 = []
images2 = []

#Taking_Input_of_Images_from_first_camera_in_Arrays
mypath='/Users/anveshjadon/Desktop/Python/task1/1'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = np.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
  images1.append(cv2.imread( join(mypath,onlyfiles[n])) )

#Taking_Input_of_Images_from_second_camera_in_Arrays
mypath='/Users/anveshjadon/Desktop/Python/task1/2'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = np.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
  images2.append(cv2.imread( join(mypath,onlyfiles[n])) )


##### Test Case for 1 image build for learning
#img1 = cv2.imread('/Users/anveshjadon/Desktop/Python/task1/test1.jpg',0)
#img2 = cv2.imread('/Users/anveshjadon/Desktop/Python/task1/test2.jpg',0)

##### Imshow part not working due to some error in installation of OpenCV, work to fix this
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Defining Parameters
speckle_window_size = 0
speckle_range = 0
P1 = 0
P2 = 0
max_pixel_disparity=16
siz = [5, 15, 17]


#Loops for finding disparities in images
for n in range(0,len(images1)):
	for s in range(0,len(siz)):
		stereo = cv2.StereoSGBM_create(minDisparity=0,numDisparities=max_pixel_disparity, blockSize=siz[s])
		disparity = stereo.compute(images1[n],images2[n])

###### Improve and Understand SGBM function and understand why a fixed matrix of disparity is coming out.