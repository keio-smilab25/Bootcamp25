import cv2
import numpy as np

# 画像の読み込み
img = cv2.imread("/Users/odahiroomi/Desktop/画像処理100本ノック/Gasyori100knock-1/assets/imori.jpg")

# 元画像のサイズ取得
H, W, C = img.shape

# 拡大縮小率
a = 1.3  # x方向
d = 0.8  # y方向

# 平行移動量
tx = 30
ty = -30

H_new = int(H * d)
W_new = int(W * a)

# 出力画像の準備（黒で初期化）
out1 = np.zeros((H_new, W_new, C), dtype=np.uint8)
out2 = np.zeros((H_new, W_new, C), dtype=np.uint8)

# Backward Mapping (出力座標から入力座標を計算)
for y_out in range(H_new):
    for x_out in range(W_new):
        
        # --- (1) リサイズのみ ---
        x_in1 = int(x_out / a)
        y_in1 = int(y_out / d)

        if 0 <= x_in1 < W and 0 <= y_in1 < H:
            out1[y_out, x_out] = img[y_in1, x_in1]

        # --- (2) リサイズ + 平行移動 ---
        x_in2 = int((x_out - tx) / a)
        y_in2 = int((y_out - ty) / d)

        if 0 <= x_in2 < W and 0 <= y_in2 < H:
            out2[y_out, x_out] = img[y_in2, x_in2]

# 結果の表示
cv2.imshow("result1 (Resize)", out1)
cv2.waitKey(0)
cv2.imshow("result2 (Resize + Translate)", out2)
cv2.waitKey(0)
cv2.destroyAllWindows()