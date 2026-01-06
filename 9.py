import cv2
import numpy as np

img = cv2.imread("/Users/odahiroomi/Desktop/画像処理100本ノック/Gasyori100knock-1/Question_01_10/imori_noise.jpg")
ans = np.zeros_like(img)
zero_pad_img = np.pad(img, [(1, 1), (1, 1), (0, 0)], "constant")

K = (1 / 16) * np.array([[[1,1,1],[2,2,2],[1,1,1]],[[2,2,2],[4,4,4],[2,2,2]],[[1,1,1],[2,2,2],[1,1,1]]])

for height_i in range(ans.shape[0]):
    for width_i in range(ans.shape[1]):
        ans[height_i, width_i] = np.sum(K * zero_pad_img[height_i:height_i + 3, width_i:width_i + 3], axis = (0,1))
        
cv2.imshow("imori", ans)
cv2.waitKey(0)