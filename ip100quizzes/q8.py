"""
Image Processing 100 Knock - Q8: Max Pooling
This module divides the image into 8x8 grids and replaces each sector
with the maximum pixel value of that area.
"""

# pylint: disable=no-member

import cv2
import numpy as np


def max_pooling(img, kernel_size=8):
    """
    画像を8x8の領域ごとに最大値で埋める
    """
    out = img.copy()
    height, width, channels = img.shape

    for i in range(height // kernel_size):
        for j in range(width // kernel_size):
            y_start, y_end = kernel_size * i, kernel_size * (i + 1)
            x_start, x_end = kernel_size * j, kernel_size * (j + 1)

            for c in range(channels):
                v_max = np.max(out[y_start:y_end, x_start:x_end, c])
                out[y_start:y_end, x_start:x_end, c] = v_max

    return out


def main():
    """
    メイン関数
    """
    img = cv2.imread("imori.jpg")
    if img is None:
        print("Image not found.")
        return

    out = max_pooling(img, kernel_size=8)

    cv2.imshow("Result", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
