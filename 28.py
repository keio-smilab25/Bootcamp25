import cv2
import numpy as np

# 画像の読み込み
img = cv2.imread("/Users/odahiroomi/Desktop/画像処理100本ノック/Gasyori100knock-1/assets/imori.jpg")

# 画像の高さ、幅、チャンネル数を取得
H, W, C = img.shape

# 平行移動量 (x: +30, y: -30)
tx = 30
ty = -30

# 出力画像の準備（黒で初期化）
out = np.zeros((H, W, C), dtype=np.uint8)

# 出力画像の各画素についてループ（Backward Mapping）
# 出力座標 (y_out, x_out) から 元の座標 (y_in, x_in) を求める
for y_out in range(H):
    for x_out in range(W):
        x_in = x_out - tx
        y_in = y_out - ty

        # 元の画像の範囲内に収まっているかチェック
        if 0 <= x_in < W and 0 <= y_in < H:
            out[y_out, x_out] = img[y_in, x_in]

# 結果の表示
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()