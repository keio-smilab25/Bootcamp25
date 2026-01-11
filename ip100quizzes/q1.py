"""
Image Processing 100 Knock - Q1: Channel Swapping
This module implements a function to swap BGR channels to RGB.
"""

# pylint: disable=no-member

import cv2
import numpy as np


def bgr2rgb(img):
    """
    bgrをrgbに並べ替える
    """
    red = img[:, :, 2].copy()
    green = img[:, :, 1].copy()
    blue = img[:, :, 0].copy()

    out = np.zeros_like(img)
    out[:, :, 0] = red
    out[:, :, 1] = green
    out[:, :, 2] = blue

    return out


def main():
    """
    メイン処理
    """
    img = cv2.imread("imori.jpg")
    out = bgr2rgb(img)

    cv2.imshow("Result", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
