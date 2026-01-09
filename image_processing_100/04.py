import cv2

img = cv2.imread("imori.jpg")

b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
gray = gray.astype("uint8")

out = gray.copy()

max_sigma = 0
max_t = 0