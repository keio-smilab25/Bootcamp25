import cv2
import numpy as np

img = cv2.imread("imori_noise.jpg")
H, W, C = img.shape

K_size = 3
sigma = 1.3
pad = K_size // 2

K = np.zeros((K_size, K_size), dtype=float)

for y in range(-pad, pad + 1):
    for x in range(-pad, pad + 1):
        val = (x**2 + y**2) / (2 * sigma**2)
        K[y + pad, x + pad] = (1 / (2 * np.pi * sigma**2)) * np.exp(-val)

K /= K.sum()

# zero padding
img_pad = np.pad(img, ((pad, pad), (pad, pad), (0, 0)), "constant")
out = np.zeros((H, W, C), dtype=float)

for y in range(H):
    for x in range(W):
        for c in range(C):
            out[y, x, c] = np.sum(img_pad[y : y + K_size, x : x + K_size, c] * K)

out = np.clip(out, 0, 255).astype("uint8")
cv2.imshow("window", out)
cv2.waitKey(0)
