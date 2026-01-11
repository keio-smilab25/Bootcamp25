"""
Image Processing 100 Knock - Q28: Affine Transformation (Translation)
This module performs image translation using an affine transformation matrix.
The image is shifted by tx=+30 and ty=-30.
"""

# pylint: disable=no-member

import cv2
import numpy as np


def affine_translation(img, tx=30, ty=-30):
    """
    アフィン変換の逆変換を用いて画像を平行移動させる。
    """
    height, width, channels = img.shape
    out = np.zeros((height, width, channels), dtype=np.uint8)

    for y_out in range(height):
        for x_out in range(width):
            x_in = x_out - tx
            y_in = y_out - ty

            if 0 <= x_in < width and 0 <= y_in < height:
                out[y_out, x_out] = img[y_in, x_in]

    return out


def main():
    """
    メイン関数
    """
    img = cv2.imread("imori.jpg")
    if img is None:
        print("Image not found.")
        return

    out = affine_translation(img, tx=30, ty=-30)

    cv2.imshow("Result", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
