import cv2
import numpy as np

# 画像の読み込み
img = cv2.imread("/Users/odahiroomi/Desktop/画像処理100本ノック/Gasyori100knock-1/assets/imori.jpg")

# 画像の高さ、幅、チャンネル数を取得
H, W, C = img.shape

angle = -30
rad = np.deg2rad(angle) # ラジアンに変換
c = np.cos(rad)
s = np.sin(rad)

# 出力画像の準備（黒で初期化）
out1 = np.zeros((H, W, C), dtype=np.uint8)
out2 = np.zeros((H, W, C), dtype=np.uint8)

for y_out in range(H):
    for x_out in range(W):
        # 逆変換（出力座標 -> 入力座標）
        x_in = int(x_out * c + y_out * s)
        y_in = int(-x_out * s + y_out * c)

        # 範囲内であれば画素値を代入
        if 0 <= x_in < W and 0 <= y_in < H:
            out1[y_out, x_out] = img[y_in, x_in]

# 回転の中心座標
cx = W / 2
cy = H / 2

for y_out in range(H):
    for x_out in range(W):
        # 1. 中心を原点(0,0)に移動
        tx = x_out - cx
        ty = y_out - cy
        
        # 2. 回転（逆変換）
        x_rot = tx * c + ty * s
        y_rot = -tx * s + ty * c
        
        # 3. 中心を元の位置(cx, cy)に戻す
        x_in = int(x_rot + cx)
        y_in = int(y_rot + cy)

        # 範囲内であれば画素値を代入
        if 0 <= x_in < W and 0 <= y_in < H:
            out2[y_out, x_out] = img[y_in, x_in]

# 結果の表示
cv2.imshow("result1 (Origin)", out1)
cv2.waitKey(0)
cv2.imshow("result2 (Center)", out2)
cv2.waitKey(0)
cv2.destroyAllWindows()