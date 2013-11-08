#!/usr/bin/env python
#
# (c) 2013 Merly Escalona <merlyescalona@uvigo.es>
#          Ivan Gomez-Conde <ivangconde@uvigo.es>
#     09.10.2013 Example for ESEI Dojo OpenCV
#     Description: Reading and showing video file.
#
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
cv2.namedWindow('Video')
# Reading 1 frame
success,frame=video.read()
while success:
  # Saying that we are using the window named "Video" and 
  # we are going to show the image in "frame"
  cv2.imshow('Video',frame)     
  success,frame=video.read()
  
  # In order to "watch" the video, we have to wait some time
  # otherwise we would not see anything
  keycode = cv2.waitKey(30)
  if keycode == 27:
    break
cv2.destroyWindow('Video')
