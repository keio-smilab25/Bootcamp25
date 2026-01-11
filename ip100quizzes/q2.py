"""
Image Processing 100 Knock - Q2: Grayscale Conversion
This module implements grayscale conversion using the Luma coding
coefficients (ITU-R Rec.BT.709): Y = 0.2126R + 0.7152G + 0.0722B.
"""

# pylint: disable=no-member

import cv2
import numpy as np


def rgb2gray(img):
    """
    画像をグレースケールにする
    """
    red = img[:, :, 2].copy()
    green = img[:, :, 1].copy()
    blue = img[:, :, 0].copy()

    y = 0.2126 * red + 0.7152 * green + 0.0722 * blue

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
    out = rgb2gray(img)

    cv2.imshow("Result", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
