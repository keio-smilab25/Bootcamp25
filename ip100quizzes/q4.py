"""
Image Processing 100 Knock - Q4: Otsu's Binarization
This module implements Otsu's method to automatically determine
the optimal threshold for binarization.
"""

# pylint: disable=no-member

import cv2
import numpy as np


def otsu_binarization(img):
    """
    大津の2値化で画像を2値化する
    """
    red = img[:, :, 2].copy()
    green = img[:, :, 1].copy()
    blue = img[:, :, 0].copy()
    y = 0.2126 * red + 0.7152 * green + 0.0722 * blue
    y = y.astype(np.uint8)

    h, w = y.shape
    max_sb2 = 0
    best_t = 0

    # 全画素数
    total_pixels = h * w

    for t in range(1, 256):
        v0 = y[y < t]
        v1 = y[y >= t]

        w0 = len(v0) / total_pixels
        w1 = len(v1) / total_pixels

        if w0 == 0 or w1 == 0:
            continue

        m0 = np.mean(v0)
        m1 = np.mean(v1)
        sb2 = w0 * w1 * ((m0 - m1) ** 2)

        # クラス間分散が最大となる閾値を保持
        if sb2 > max_sb2:
            max_sb2 = sb2
            best_t = t

    print(f"Optimal threshold: {best_t}")

    # 決定した閾値で二値化
    out = np.where(y < best_t, 0, 255).astype(np.uint8)
    final_out = cv2.merge([out, out, out])

    return final_out


def main():
    """
    メイン関数
    """
    img = cv2.imread("imori.jpg")
    if img is None:
        print("Image not found.")
        return

    out = otsu_binarization(img)

    cv2.imshow("Result", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
