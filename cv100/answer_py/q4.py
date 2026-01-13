import cv2
import numpy as np

def gray_scale(img):
    r = img[:, :, 2].copy()
    g = img[:, :, 1].copy()
    b = img[:, :, 0].copy()

    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    gray = np.clip(y, 0, 255).astype(np.uint8)

    return gray


def otsu_binarization(img):
    h, w = img.shape
    total_pixels = h * w

    max_sigma = 0
    best_threshold= 0

    for t in range(1, 255):
        class0 = img[img < t]
        class1 = img[img >= t]

        w0 = class0.size / total_pixels
        w1 = class1.size / total_pixels

        if class0.size == 0 or class1.size == 0:
            continue

        m0 = class0.mean()
        m1 = class1.mean()

        sigma = w0 * w1 * (m0 - m1) ** 2

        if sigma > max_sigma:
            max_sigma = sigma
            best_threshold = t

    print(f"threshold: {best_threshold}")

    out = gray.copy()
    th = best_threshold
    out[out < th] = 0
    out[out >= th] = 255

    return out


img = cv2.imread("../../Gasyori100knock/Question_01_10/imori.jpg")

gray = gray_scale(img)
out = otsu_binarization(gray)

cv2.imwrite("../answers_image/answer_4.jpg", out)