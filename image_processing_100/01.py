import cv2

img = cv2.imread("imori.jpg")

b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

img[:, :, 0] = r
img[:, :, 1] = g
img[:, :, 2] = b

cv2.imshow("window", img)
cv2.waitKey(0)
