#!/usr/bin/env python
#
# (c) 2013 Merly Escalona   <merlyescalona@uvigo.es>
#          Ivan Gomez-Conde <ivangconde@uvigo.es>
#     09.10.2013 Example for ESEI Dojo OpenCV
#     Description: Image visualization

import cv2

imgInput = cv2.imread("data/opencv.jpg")
print imgInput
cv2.namedWindow('Image')
cv2.imshow('Image',imgInput)
cv2.waitKey()

