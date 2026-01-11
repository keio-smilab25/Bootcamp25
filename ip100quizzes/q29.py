"""
Image Processing 100 Knock - Q29: Affine Transformation (Scaling & Translation)
This module performs image resizing
and translation using affine transformation.
1. Resize: Scale x1.3, y0.8 (Change output image size)
2. Scale & Translate: x1.3, y0.8 AND tx+30, ty-30
"""

# pylint: disable=no-member

import cv2
import numpy as np


def affine_transform(img, a, b, c, d, tx, ty, out_size=None):
    """
    アフィン変換の逆変換を用いて画像を変換する。
    out_sizeが指定されない場合は、入力画像と同じサイズを出力する。
    """
    h_in, w_in, channels = img.shape

    if out_size:
        w_out, h_out = out_size
    else:
        w_out, h_out = w_in, h_in

    out = np.zeros((h_out, w_out, channels), dtype=np.uint8)

    det = a * d - b * c

    for y_out in range(h_out):
        for x_out in range(w_out):
            new_x = (d * (x_out - tx) - b * (y_out - ty)) / det
            new_y = (-c * (x_out - tx) + a * (y_out - ty)) / det

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

    # (1)
    w_new, h_new = int(w * 1.3), int(h * 0.8)
    out1 = affine_transform(img, a=1.3, b=0, c=0, d=0.8, tx=0, ty=0,
                            out_size=(w_new, h_new))
    # (2)
    out2 = affine_transform(img, a=1.3, b=0, c=0, d=0.8, tx=30, ty=-30,
                            out_size=(w_new, h_new))

    cv2.imshow("Resized (1)", out1)
    cv2.imshow("Resized & Translated (2)", out2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
