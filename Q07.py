import cv2
import numpy as np

img = cv2.imread("imori.jpg")

grid = 8
H, W, C= img.shape

for h in range(H // grid):
    for w in range(W // grid):
        for c in range(C):
            img[h*grid:h*grid+grid, w*grid:w*grid+grid, c] = np.mean(img[h*grid:h*grid+grid, w*grid:w*grid+grid, c])

cv2.imshow("window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()