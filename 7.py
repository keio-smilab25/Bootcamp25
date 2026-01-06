import cv2
import numpy as np

# 画像の読み込み
img = cv2.imread("/Users/odahiroomi/Desktop/画像処理100本ノック/Gasyori100knock-1/assets/imori.jpg")

# 画像の高さと幅を取得
h, w, c = img.shape

# グリッドのサイズ (8x8)
step = 8

# 高さ方向にstep(8)刻みでループ
for y in range(0, h, step):
    # 幅方向にstep(8)刻みでループ
    for x in range(0, w, step):
        block = img[y:y+step, x:x+step]

        mean_val = np.mean(block, axis=(0, 1)).astype(int)
        
        img[y:y+step, x:x+step] = mean_val

# 画像の表示
cv2.imshow("imori", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
