#!/usr/bin/env python
#
# (c) 2013 Merly Escalona   <merlyescalona@uvigo.es>
#          Ivan Gomez-Conde <ivangconde@uvigo.es>
#     09.10.2013 Example for ESEI Dojo OpenCV
#     Description: Image transformation using thresholds

import cv2
 
# Filename 
filename="data/cherries.jpg"
img = cv2.imread(filename,0)
ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
#ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
#ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('Thresholding',thresh)     
keycode = cv2.waitKey()
if keycode == 27:
  break
