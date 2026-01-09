import cv2

img = cv2.imread("imori.jpg")

H, W, C = img.shape

grid_size = 8

out = img.copy()

for y in range(0, H, grid_size):
    for x in range(0, W, grid_size):
        block = img[y : y + grid_size, x : x + grid_size]
        mean_color = block.mean(axis=(0, 1)).astype("uint8")
        out[y : y + grid_size, x : x + grid_size] = mean_color

cv2.imshow("window", out)
cv2.waitKey(0)
