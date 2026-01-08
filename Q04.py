import cv2
import numpy as np

img = cv2.imread("imori.jpg")

b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

gray = 0.2126 * r + 0.7152 * g + 0.0722 * b

h, w = gray.shape
max_s_b = 0.
true_th = 0
for th in range(256):
    v0 = gray[gray < th]
    m0 = np.mean(v0) if len(v0) > 0 else 0
    w0 = len(v0) / (h * w)
    v1 = gray[gray >= th]
    m1 = np.mean(v1) if len(v1) > 0 else 0
    w1 = len(v1) / (h * w)
    s_b = w0 * w1 * (m0 - m1)**2
    if s_b > max_s_b:
        true_th = th
        max_s_b = s_b

gray[gray < true_th] = 0
gray[gray >= true_th] = 255

gray = gray.astype(np.uint8)

cv2.imshow("window", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
