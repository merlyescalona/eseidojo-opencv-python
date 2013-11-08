#!/usr/bin/env python  
#
# (c)  2013 Merly Escalona   <merlyescalona@uvigo.es>
#           Ivan Gomez-Conde <ivangconde@uvigo.es>
#     09.10.2013 Example for ESEI Dojo OpenCV
#     Description: Reading from webcam


import cv2
 
video = cv2.VideoCapture(0)
fps = video.get(cv2.cv.CV_CAP_PROP_FPS)

size=(int(video.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),\
      int(video.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
fps=25 # Depends on video format (NSTC | PAL)
videoWriter=cv2.VideoWriter('webcamvideo.avi', cv2.cv.CV_FOURCC('I','4','2','0'),fps, size)

success, frame = video.read()
counter=1
while success: # Loop until there are no more frames.
        success, frame = video.read()
        videoWriter.write(frame)
        counter+=1

print "fps: ",fps,"\nsize: ",size, counter

