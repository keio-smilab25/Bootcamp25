import cv2
import numpy as np

img = cv2.imread("imori.jpg")

b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
gray = gray.astype("uint8")

max_sigma = 0
max_t = 0

for t in range(1, 256):
    v0 = gray[gray < t]
    v1 = gray[gray >= t]

    n0 = len(v0)
    n1 = len(v1)

    if n0 == 0 or n1 == 0:
        continue

    m0 = np.mean(v0)
    m1 = np.mean(v1)
    w0 = n0 / (n0 + n1)
    w1 = n1 / (n0 + n1)

    sigma = w0 * w1 * (m0 - m1) ** 2

    if sigma > max_sigma:
        max_sigma = sigma
        max_t = t

th = max_t
out = gray.copy()
out[gray > th] = 255
out[gray <= th] = 0

print(th)

cv2.imshow("window", out)
cv2.waitKey(0)

