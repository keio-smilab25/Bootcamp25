import cv2
import numpy as np

img = cv2.imread("/Users/odahiroomi/Desktop/画像処理100本ノック/Gasyori100knock-1/assets/imori.jpg")
img[:,:] = img[:,:,(2,1,0)]

cv2.imshow("imori", img)
cv2.waitKey(0)