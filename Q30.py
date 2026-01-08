import cv2
import numpy as np

img = cv2.imread("imori.jpg").astype(np.float32)

H, W, C = img.shape

def affine1(img, a, b, c, d, tx, ty):
    H_new = int(H)
    W_new = int(W)
    result = np.zeros((H_new, W_new, C), dtype=np.uint8)

    x_new, y_new = np.meshgrid(np.arange(W_new), np.arange(H_new))

    x = ((d * (x_new + 1) - b * (y_new + 1)) / (a*d - b*c) - tx - 1).astype(np.int32)
    y = ((-c * (x_new + 1) + a * (y_new + 1)) / (a*d - b*c) - ty - 1).astype(np.int32)

    mask = (x >= 0) & (x < W) & (y >= 0) & (y < H)
    result[y_new[mask], x_new[mask]] = img[y[mask], x[mask]]

    return result

def affine2(img, a, b, c, d, tx, ty):
    H_new = int(H)
    W_new = int(W)
    result = np.zeros((H_new, W_new, C), dtype=np.uint8)

    x_new, y_new = np.meshgrid(np.arange(W_new), np.arange(H_new))
    cx = W/2
    cy = H/2

    _x = x_new - cx
    _y = y_new - cy

    x = ((d * _x - b * _y) / (a*d - b*c) - tx + cx - 1).astype(np.int32)
    y = ((-c * _x + a * _y) / (a*d - b*c) - ty + cy - 1).astype(np.int32)

    mask = (x >= 0) & (x < W) & (y >= 0) & (y < H)
    result[y_new[mask], x_new[mask]] = img[y[mask], x[mask]]

    return result

cos = np.cos(np.pi / 6)
sin = np.sin(np.pi / 6)

img1 = affine1(img, cos, sin, -sin, cos, 0, 0)
cv2.imshow("window", img1)
cv2.waitKey(0)
img2 = affine2(img, cos, sin, -sin, cos, 0, 0)
cv2.imshow("result", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()