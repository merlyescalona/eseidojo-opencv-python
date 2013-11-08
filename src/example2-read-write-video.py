#!/usr/bin/env python
#
# (c) 2013 Merly Escalona   <merlyescalona@uvigo.es>
#          Ivan Gomez-Conde <ivangconde@uvigo.es>
#     09.10.2013 Example for ESEI Dojo OpenCV
#     Description: Read/write a video from OpenCV with python


import cv2

video = cv2.VideoCapture("data/aquarium.mp4")
fps = video.get(cv2.cv.CV_CAP_PROP_FPS)

# Properties: 
# http://docs.opencv.org/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-get
size=(int(video.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),\
      int(video.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

# Video Writer - Codecs Info:
# http://docs.opencv.org/modules/highgui/doc/reading_and_writing_images_and_video.html?highlight=video%20writer%20fourcc#videowriter-videowriter
# Video Codecs 
# http://www.fourcc.org/codecs.php
videoWriter=cv2.VideoWriter('outputvideo.avi', cv2.cv.CV_FOURCC('I','4','2','0'),fps, size)

success, frame = video.read()
counter=1
while success: # Loop until there are no more frames.
	videoWriter.write(frame)
	success, frame = video.read()
	print "Writing frame",counter
	counter+=1

print "fps: ",fps,"\nsize: ",size
