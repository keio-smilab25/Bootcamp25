import cv2
import numpy as np

img = cv2.imread("imori.jpg")
H, W, C = img.shape

# ラジアンに変換
A = 30 * np.pi / 180.0

out1 = np.zeros((H, W, C), dtype=np.uint8)
for y_new in range(H):
    for x_new in range(W):
        x_old = int(x_new * np.cos(A) - y_new * np.sin(A))
        y_old = int(x_new * np.sin(A) + y_new * np.cos(A))

        if 0 <= x_old < W and 0 <= y_old < H:
            out1[y_new, x_new] = img[y_old, x_old]
        else:
            out1[y_new, x_new] = 0
cv2.imshow("window1", out1)
cv2.waitKey(0)

out2 = np.zeros((H, W, C), dtype=np.uint8)

cx = W / 2
cy = H / 2
cx_new = W / 2
cy_new = H / 2

for y_new in range(H):
    for x_new in range(W):

        tx = x_new - cx_new
        ty = y_new - cy_new

        x_old = int(tx * np.cos(A) + ty * np.sin(A))
        y_old = int(-tx * np.sin(A) + ty * np.cos(A))

        x_old = int(np.round(x_old + cx))
        y_old = int(np.round(y_old + cy))

        if 0 <= x_old < W and 0 <= y_old < H:
            out2[y_new, x_new] = img[y_old, x_old]

cv2.imshow("window2", out2)
cv2.waitKey(0)
