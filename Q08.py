import cv2
import numpy as np

def max_pooling(img, grid=8):
    h, w, c = img.shape
    for i in range(0, h, grid):
        for j in range(0, w, grid):
            for k in range(c):
                block = img[i:i+grid, j:j+grid, k]
                max_val = block.max()
                img[i:i+grid, j:j+grid, k] = max_val
    return img

def main():
    img = cv2.imread('Gasyori100knock/Question_01_10/imori.jpg')
    img = max_pooling(img, grid=8)
    cv2.imshow("window", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
