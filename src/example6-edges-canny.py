#!/usr/bin/env python
#
# (c) 2013 Merly Escalona   <merlyescalona@uvigo.es>
#          Ivan Gomez-Conde <ivangconde@uvigo.es>
#     09.10.2013 Example for ESEI Dojo OpenCV
#     Description: Edge detection filter

import sys
import cv2

video=0
if len(sys.argv) > 1:
  # Parameter?
  video=sys.argv[1]
  print "Video File: ", video
else:
  print "Using webcam"
  
# Reading video
video=cv2.VideoCapture(video)
# Creating visualization window
cv2.namedWindow('edges')
# Reading 1 frame
success,frame=video.read()

while success:
  gsFrame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
  # Using edge detection filter named Canny
  # Threholds 600, 1200,
  # ApertureSize -> size of sobel filter
  edge = cv2.Canny(gsFrame, 600, 1200, apertureSize=5)
  # this returns a binary image
  frameWEdges = frame.copy()
  # Create new image from original, where edge frame is !=0 
  # We change the color of the frame to red(which is black)
  #frameWEdges[edge != 0] = (0,255,0) # mixture of mask and image
  cv2.imshow('edges',edge) # Visualization of the mask
  #cv2.imshow('edges',frameWEdges) # visualization of the img with the mask (in green)
  success,frame=video.read()
  
  # In order to "watch" the video, we have to wait some time
  # otherwise we would not see anything
  keycode = cv2.waitKey(30)
  if keycode == 27:
    break
cv2.destroyWindow('edges')
