import cv2

image=cv2.imread("rohit.webp",cv2.IMREAD_UNCHANGED)
cv2.imshow("tittle",image)

cv2.waitKey(0)