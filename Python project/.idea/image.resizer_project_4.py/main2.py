import cv2

src=cv2.imread("rohit.webp",cv2.IMREAD_UNCHANGED)
cv2.imshow("title",src)

# percent by which the image is resized
scale_percent=50

#calculate the 50 percent of original dimesions
new_width=int(src.shape[1]*scale_percent/100)
new_height=int(src.shape[0]*scale_percent/100)

#dsize
dsize=(new_width,new_height)

#resize image

output=cv2.resize(src,dsize)

cv2.imwrite('newImage.png',output)
cv2.waitKey(0)































