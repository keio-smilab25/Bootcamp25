import cv2
import numpy as np

def gaussian_filter(img, kernel_size=3, sigma=1.3):
    h, w, c = img.shape
    kernel = np.zeros((kernel_size, kernel_size))
    center = kernel_size // 2
    img_pad = np.pad(img, [(center, center), (center, center), (0, 0)], 'edge') #Pading
    for i in range(kernel_size):
        for j in range(kernel_size):
            x, y = i - center, j - center
            kernel[i, j] = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    kernel /= np.sum(kernel)
    filtered_img = np.zeros_like(img)
    for k in range(c):
        for i in range(h):
            for j in range(w):
                filtered_img[i, j, k] = np.sum(kernel * img_pad[i : i + kernel_size, j : j + kernel_size, k])
    return filtered_img.astype('uint8')

def main():
    img = cv2.imread('Gasyori100knock/Question_01_10/imori_noise.jpg')
    img = gaussian_filter(img)
    cv2.imshow("window", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
