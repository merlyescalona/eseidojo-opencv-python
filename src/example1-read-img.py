#!/usr/bin/env python
#
# (c) 2013 Merly Escalona   <merlyescalona@uvigo.es>
#          Ivan Gomez-Conde <ivangconde@uvigo.es>
#     09.10.2013 Example for ESEI Dojo OpenCV
#     Description: Reading and writing images

import cv2

imageInput = cv2.imread("data/cherries.jpg")
print imageInput

imageOutput = cv2.imwrite("data/copyCherries.jpg",imageInput)

