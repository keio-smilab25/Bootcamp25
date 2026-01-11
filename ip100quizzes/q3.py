"""
Image Processing 100 Knock - Q3: Binarization
This module implements image binarization. It first converts the image 
to grayscale and then applies a threshold of 128 to produce a black 
and white output.
"""

# pylint: disable=no-member

import cv2
import numpy as np


def binarization(img):
    """
    画像を2値化する
    """
    red = img[:, :, 2].copy()
    green = img[:, :, 1].copy()
    blue = img[:, :, 0].copy()

    y = 0.2126 * red + 0.7152 * green + 0.0722 * blue
    y = np.where(y < 128, 0, 255)

    out = np.zeros_like(img)
    out[:, :, 0] = y
    out[:, :, 1] = y
    out[:, :, 2] = y

    return out


def main():
    """
    メイン処理
    """

    img = cv2.imread("imori.jpg")
    out = binarization(img)

    cv2.imshow("Result", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
