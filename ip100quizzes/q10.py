"""
Image Processing 100 Knock - Q10: Median Filter
This module applies a 3x3 Median filter to reduce salt-and-pepper noise.
Zero padding is applied to maintain the original image size.
"""

# pylint: disable=no-member

import cv2
import numpy as np


def median_filter(img, kernel_size=3):
    """
    注目画素の3x3領域内の中央値を出力するメディアンフィルタを適用する。
    """
    height, width, channels = img.shape

    pad = kernel_size // 2
    padded_img = np.zeros((
        height + pad * 2, width + pad * 2, channels), dtype=np.float32)
    padded_img[pad: pad + height,
               pad: pad + width] = img.copy().astype(np.float32)

    out = np.zeros_like(img, dtype=np.float32)

    for y in range(height):
        for x in range(width):
            for c in range(channels):
                target_area = padded_img[y: y + kernel_size,
                                         x: x + kernel_size, c]
                out[y, x, c] = np.median(target_area)

    out = out.astype(np.uint8)
    return out


def main():
    """
    メイン関数
    """
    img = cv2.imread("imori_noise.jpg")
    if img is None:
        print("Image not found.")
        return

    out = median_filter(img, kernel_size=3)

    cv2.imshow("Result", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
