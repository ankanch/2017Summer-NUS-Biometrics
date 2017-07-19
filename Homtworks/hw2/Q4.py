import cv2
import numpy as np

# read image
lz = cv2.imread("./bee.png")
lzz = cv2.imread("./lz.jpg")   # my face

# convert to HSV
lz = cv2.cvtColor(lz, cv2.COLOR_BGR2HSV)
lzz = cv2.cvtColor(lzz,cv2.COLOR_BGR2HSV)
#
mask = cv2.inRange(lz,(25,0,0),(35,255,255))
face_mask = cv2.inRange(lzz,(10,0,0),(90,255,255))
cv2.imshow("mask",mask)
cv2.imshow("face of long zhang",face_mask)
cv2.waitKey()
cv2.imwrite("./q4_image_mask_of_flowers_bee.png",mask)
cv2.imwrite("./q4_image_mask_of_face_of_long_zhang.jpg",face_mask)

# color transform of bee.png
H = lz[:,:,0].copy()
H_bg = cv2.bitwise_and(H, 255-mask)
H_roi = cv2.bitwise_and(H+150, mask)
H = cv2.bitwise_or(H_bg, H_roi)
print(H,lz[:,:,0])
lz[:,:,0] = H
lz = cv2.cvtColor(lz,cv2.COLOR_HSV2BGR)
# transforms for my face
H = lzz[:,:,0].copy()
H_bg = cv2.bitwise_and(H, 255-face_mask)
H_roi = cv2.bitwise_and(H-H, face_mask)
H = cv2.bitwise_or(H_bg, H_roi)
lzz[:,:,0] = H
lzz = cv2.cvtColor(lzz,cv2.COLOR_HSV2BGR)

# show and save final pictures
cv2.imshow("new img",lz)
cv2.imshow("new face of long zhang",lzz)
cv2.waitKey()
cv2.imwrite("./q4_megenta_flower_bee.png",lz)
cv2.imwrite("./q4_read_face_of_long_zhang.png",lzz)
