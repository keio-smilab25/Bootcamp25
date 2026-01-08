import cv2
import numpy as np

img = cv2.imread("imori_noise.jpg")

H, W, C = img.shape

img_pad = np.zeros((H + 2, W + 2, C))
img_pad[1:H+1, 1:W+1, :] = img.copy()

for h in range(1, H+1):
    for w in range(1, W+1):
        for c in range(C):
            img[h-1, w-1, c] = np.median(img_pad[h-1:h+2, w-1:w+2, c])

cv2.imshow("window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()