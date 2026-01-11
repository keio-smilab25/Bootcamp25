"""
Image Processing 100 Knock - Q9: Gaussian Filter
This module applies a 3x3 Gaussian filter with sigma=1.3 to reduce noise.
Zero padding is applied to maintain the original image size.
"""

# pylint: disable=no-member

import cv2
import numpy as np


def gaussian_filter(img, kernel_size=3, sigma=1.3):
    """
    ガウシアンフィルタ(3x3, sigma=1.3)を実装し、平滑化を行う。
    """
    height, width, channels = img.shape

    pad = kernel_size // 2
    out = np.zeros((height + pad * 2, width + pad * 2, channels),
                   dtype=np.float32)
    out[pad: pad + height, pad: pad + width] = img.copy().astype(np.float32)

    kernel = np.zeros((kernel_size, kernel_size), dtype=np.float32)
    for y in range(-pad, -pad + kernel_size):
        for x in range(-pad, -pad + kernel_size):
            kernel[y + pad, x + pad] = np.exp(
                -(x**2 + y**2) / (2 * (sigma**2)))
    kernel /= (2 * np.pi * sigma * sigma)
    kernel /= kernel.sum()  # 正規化

    tmp = out.copy()
    for y in range(height):
        for x in range(width):
            for c in range(channels):
                out[pad + y, pad + x, c] = np.sum(
                    kernel * tmp[y: y + kernel_size, x: x + kernel_size, c]
                )

    out = np.clip(
        out[pad: pad + height, pad: pad + width], 0, 255).astype(np.uint8)
    return out


def main():
    """
    メイン処理：ノイズの乗った画像を読み込み、ガウシアンフィルタを適用する。
    """
    img = cv2.imread("imori_noise.jpg")
    if img is None:
        print("Image not found.")
        return

    out = gaussian_filter(img, kernel_size=3, sigma=1.3)

    cv2.imshow("Result", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
