import cv2

img = cv2.imread("imori.jpg")

b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

gray = 0.2126 * r + 0.7152 * g + 0.0722 * b

img[:, :, 0] = gray
img[:, :, 1] = gray
img[:, :, 2] = gray

cv2.imshow("window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



