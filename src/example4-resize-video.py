#!/usr/bin/env python
#
# (c) 2013 Merly Escalona   <merlyescalona@uvigo.es>
#          Ivan Gomez-Conde <ivangconde@uvigo.es>
#     09.10.2013 Example for ESEI Dojo OpenCV
#     Description: Resizing
#
import sys
import cv2

video=0
if len(sys.argv) > 1:
  video=sys.argv[1]
  print "Video File: ", video
else:
  print "Using webcam"
  
# Reading video
video=cv2.VideoCapture(video)
# Creating visualization window
cv2.namedWindow('VideoResized')
# Reading 1 frame
success,frame=video.read()
# Getting Size
currentSize=(\
  (int(video.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),\
  int(video.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))))
print "Original frame size: ", currentSize
newSize=(\
  int(currentSize[0]-(currentSize[0]*0.5)),\
  int(currentSize[1]-(currentSize[1]*0.5)))
print "New frame size: ", newSize
  
while success:
  # Saying that we are using the window named "Video" and 
  # we are going to show the image in "frame"
  newFrame=cv2.resize(frame, newSize,interpolation=cv2.INTER_LINEAR)
  cv2.imshow('VideoResized',newFrame)
  success,frame=video.read()
  # In order to "watch" the video, we have to wait some time
  # otherwise we would not see anythin
  keycode = cv2.waitKey(30)
  if keycode == 27:
    break
cv2.destroyWindow('VideoResized')
