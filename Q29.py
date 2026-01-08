import cv2
import numpy as np

img = cv2.imread("imori.jpg")

H, W, C = img.shape

def affine(img, a, b, c, d, tx, ty):
    H_new = int(H * d)
    W_new = int(W * a)
    result = np.zeros((H_new, W_new, C), dtype=np.uint8)

    x_new, y_new = np.meshgrid(np.arange(W_new), np.arange(H_new))

    x = ((d * (x_new + 1) - b * (y_new + 1)) / (a*d - b*c) - tx - 1).astype(np.int32)
    y = ((-c * (x_new + 1) + a * (y_new + 1)) / (a*d - b*c) - ty - 1).astype(np.int32)

    mask = (x >= 0) & (x < W) & (y >= 0) & (y < H)
    result[y_new[mask], x_new[mask]] = img[y[mask], x[mask]]

    return result

img1 = affine(img, 1.3, 0, 0, 0.8, 0, 0)
img2 = affine(img, 1.3, 0, 0, 0.8, 30, -30)

cv2.imshow("window", img1)
cv2.waitKey(0)
cv2.imshow("window", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()