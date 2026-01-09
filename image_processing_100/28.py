import cv2
import numpy as np

img = cv2.imread("imori.jpg")
H, W, C = img.shape

tx = 30
ty = -30

out = np.zeros((H, W, C), dtype=np.uint8)

for y_new in range(H):
    for x_new in range(W):
        x_old = x_new - tx
        y_old = y_new - ty

        if 0 <= x_old < W and 0 <= y_old < H:
            out[y_new, x_new] = img[y_old, x_old]
        else:
            out[y_new, x_new] = 0

cv2.imshow("window", out)
cv2.waitKey(0)
