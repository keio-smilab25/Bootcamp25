import cv2
import numpy as np
import matplotlib.pyplot as plt

# 画像の読み込み
img = cv2.imread("/Users/odahiroomi/Desktop/画像処理100本ノック/Gasyori100knock-1/assets/imori.jpg")

gray = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]
gray = gray.astype(np.uint8)

h, w = gray.shape
max_sigma = 0
max_t = 0

hist, bins = np.histogram(gray.ravel(), bins=256, range=(0, 256))

total_pixels = h * w

# 1から255まで閾値を走査
for t in range(1, 256):
    n0 = hist[:t].sum()
    n1 = hist[t:].sum()

    if n0 == 0 or n1 == 0:
        continue

    # 各クラスの平均値 (mu0, mu1)
    # np.arange(t) は [0, 1, ..., t-1] の配列
    mu0 = np.sum(np.arange(t) * hist[:t]) / n0
    mu1 = np.sum(np.arange(t, 256) * hist[t:]) / n1

    w0 = n0 / total_pixels
    w1 = n1 / total_pixels
    sigma = w0 * w1 * ((mu0 - mu1) ** 2)

    if sigma > max_sigma:
        max_sigma = sigma
        max_t = t
        
# 求めた閾値で二値化
th_img = gray.copy()
th_img[th_img < max_t] = 0
th_img[th_img >= max_t] = 255

# 結果の表示
plt.figure(figsize=(10, 5))

# ヒストグラム表示
plt.subplot(1, 2, 1)
plt.hist(gray.ravel(), bins=255, rwidth=0.8, range=(0, 255))
plt.axvline(x=max_t, color='red', linestyle='--')
plt.title(f"Histogram (Threshold = {max_t})")
plt.xlabel('value')
plt.ylabel('appearance')

# 画像表示
plt.subplot(1, 2, 2)
plt.imshow(th_img, cmap='gray')
plt.title("Otsu's Method Result")
plt.axis('off')

plt.show()