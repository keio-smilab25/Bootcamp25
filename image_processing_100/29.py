import cv2
import numpy as np

img = cv2.imread("imori.jpg")
H, W, C = img.shape

a, d, tx, ty = 1.3, 0.8, 30, -30

H_new = int(H * d)
W_new = int(W * a)

out = np.zeros((H_new, W_new, C), dtype=np.uint8)

for y_new in range(H_new):
    for x_new in range(W_new):
        x_old = int((x_new) / a)
        y_old = int((y_new) / d)

        if 0 <= x_old < W and 0 <= y_old < H:
            out[y_new, x_new] = img[y_old, x_old]
        else:
            out[y_new, x_new] = 0

cv2.imshow("window", out)
cv2.waitKey(0)

out2 = np.zeros((H_new, W_new, C), dtype=np.uint8)
for y_new in range(H_new):
    for x_new in range(W_new):
        x_old = int((x_new - tx) / a)
        y_old = int((y_new - ty) / d)

        if 0 <= x_old < W and 0 <= y_old < H:
            out2[y_new, x_new] = img[y_old, x_old]
        else:
            out2[y_new, x_new] = 0

cv2.imshow("window2", out2)
cv2.waitKey(0)
