import cv2

bee = cv2.imread("./bee.png")
bee = cv2.cvtColor(bee,cv2.COLOR_BGR2HSV)
#print(bee[:,:,2])
beeEqualized = cv2.equalizeHist(bee[:,:,2])
bee = cv2.cvtColor(bee,cv2.COLOR_HSV2BGR)
cv2.imshow("bee",bee)
cv2.imwrite("./q3_equalizedBee.png",bee)
cv2.waitKey()