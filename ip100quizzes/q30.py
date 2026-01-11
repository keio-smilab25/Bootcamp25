"""
Image Processing 100 Knock - Q30: Affine Transformation (Rotation)
This module performs image rotation using affine transformation.
1. Rotate 30 degrees counter-clockwise around the origin (left-top).
2. Rotate 30 degrees counter-clockwise around the image center.
"""

# pylint: disable=no-member

import cv2
import numpy as np


def affine_rotate(img, theta, tx=0, ty=0):
    """
    アフィン変換の逆変換を用いて画像を回転・平行移動させる。
    """
    h_in, w_in, channels = img.shape
    out = np.zeros((h_in, w_in, channels), dtype=np.uint8)

    rad = np.deg2rad(theta)

    a_val = np.cos(rad)
    b_val = -np.sin(rad)
    c_val = np.sin(rad)
    d_val = np.cos(rad)

    det = a_val * d_val - b_val * c_val

    for y_out in range(h_in):
        for x_out in range(w_in):
            new_x = (d_val * (x_out - tx) - b_val * (y_out - ty)) / det
            new_y = (-c_val * (x_out - tx) + a_val * (y_out - ty)) / det

            x_in = int(round(new_x))
            y_in = int(round(new_y))

            if 0 <= x_in < w_in and 0 <= y_in < h_in:
                out[y_out, x_out] = img[y_in, x_in]

    return out


def main():
    """
    メイン関数
    """
    img = cv2.imread("imori.jpg")
    if img is None:
        return

    h, w, _ = img.shape
    theta = -30

    # (1)
    out1 = affine_rotate(img, theta=theta, tx=0, ty=0)

    # (2)
    cx, cy = w / 2, h / 2
    rad = np.deg2rad(theta)
    tx = cx - (cx * np.cos(rad) - cy * np.sin(rad))
    ty = cy - (cx * np.sin(rad) + cy * np.cos(rad))

    out2 = affine_rotate(img, theta=theta, tx=tx, ty=ty)

    cv2.imshow("Rotation (Origin)", out1)
    cv2.imshow("Rotation (Center Fixed)", out2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
