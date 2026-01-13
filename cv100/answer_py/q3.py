import cv2
import numpy as np

def gray_scale(img):
    r = img[:, :, 2].copy()
    g = img[:, :, 1].copy()
    b = img[:, :, 0].copy()

    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    gray = np.clip(y, 0, 255).astype(np.uint8)

    return gray

def binarization(img):
    threshold = 128

    img[img < threshold] = 0
    img[img >= threshold] = 255

    return img

img = cv2.imread("../../Gasyori100knock/Question_01_10/imori.jpg")

img_gray = gray_scale(img)
img_binarization = binarization(img_gray)

cv2.imwrite("../answers_image/answer_3.jpg", img_binarization)