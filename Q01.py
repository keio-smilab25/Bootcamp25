import cv2

img = cv2.imread("imori.jpg")

red = img[:, :, 2].copy()
blue = img[:, :, 0].copy()

img[:, :, 0] = red
img[:, :, 2] = blue

cv2.imshow("window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()