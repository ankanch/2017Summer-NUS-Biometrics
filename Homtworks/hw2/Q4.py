import cv2
import numpy as np

# read image
lz = cv2.imread("./bee.png")
#cv2.imshow("original image",lz)
#cv2.waitKey()

# convert to HSV
lz = cv2.cvtColor(lz, cv2.COLOR_BGR2HSV)

#
mask = cv2.inRange(lz,(25,0,0),(35,255,255))
cv2.imshow("mask",mask)
cv2.waitKey()
cv2.imwrite("./q4_image_mask_of_flowers_bee.png",lz)

#
H = lz[:,:,0].copy()
H_bg = cv2.bitwise_and(H, 255-mask)
H_roi = cv2.bitwise_and(H+150, mask)
H = cv2.bitwise_or(H_bg, H_roi)
print(H,lz[:,:,0])
lz[:,:,0] = H
lz = cv2.cvtColor(lz,cv2.COLOR_HSV2BGR)
cv2.imshow("new img",lz)
cv2.waitKey()
cv2.imwrite("./q4_megenta_flower_bee.png",lz)
