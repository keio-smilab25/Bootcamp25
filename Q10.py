import cv2
import numpy as np

def median_filter(img, kernel_size=3):
    h, w, c = img.shape
    filtered_img = np.zeros_like(img)
    pad = kernel_size // 2
    img_pad = np.pad(img, [(pad, pad), (pad, pad), (0, 0)], 'edge')
    for k in range(c):
        for i in range(h):
            for j in range(w):
                filtered_img[i, j, k] = np.median(img_pad[i : i + kernel_size, j : j + kernel_size, k])
    return filtered_img.astype('uint8')

def main():
    img = cv2.imread('Gasyori100knock/Question_01_10/imori_noise.jpg')
    img = median_filter(img)
    cv2.imshow("window", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
