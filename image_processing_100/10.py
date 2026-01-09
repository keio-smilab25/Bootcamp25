import cv2
import numpy as np

img = cv2.imread("imori_noise.jpg")
H, W, C = img.shape

K_size = 3
pad = K_size // 2

img_pad = np.pad(img, ((pad, pad), (pad, pad), (0, 0)), "constant")

out = np.zeros((H, W, C), dtype=float)

for y in range(H):
    for x in range(W):
        for c in range(C):
            block = img_pad[y : y + K_size, x : x + K_size, c]
            out[y, x, c] = np.median(block)

out = out.astype(np.uint8)

cv2.imshow("result", out)
cv2.waitKey(0)
