import cv2
import numpy as np

img = cv2.imread("/Users/odahiroomi/Desktop/画像処理100本ノック/Gasyori100knock-1/assets/imori.jpg")

gray_array = img[:,:,2] * 0.2126 + img[:,:,1] * 0.7152 + img[:,:,0] * 0.0722
gray_array = gray_array.reshape(128, 128, 1)
img = gray_array.astype(np.uint8)

for height_i in range(img.shape[0]):
    for width_i in range(img.shape[1]):
        if img[height_i][width_i] < 128:
            img[height_i][width_i] = 0
        else:
            img[height_i][width_i] = 255

cv2.imshow("imori", img)
cv2.waitKey(0)