import cv2
import numpy as np

def affine_transform(img, a=1, b=0, c=0, d=1, tx=30, ty=-30):
    h, w, ch = img.shape
    h_out = int(h * d)
    w_out = int(w * a)
    transformed_img = np.zeros((h_out, w_out, ch), dtype=np.uint8)
    det = a * d - b * c
    if det == 0:
        return transformed_img
    for y_out in range(h_out):
        for x_out in range(w_out):
            x_in = (d * (x_out - tx) - b * (y_out - ty)) / det
            y_in = (-c * (x_out - tx) + a * (y_out - ty)) / det
            if 0 <= x_in < w and 0 <= y_in < h:
                transformed_img[y_out, x_out] = img[int(y_in), int(x_in)]
    return transformed_img

def main():
    img = cv2.imread('Gasyori100knock/Question_01_10/imori.jpg')
    img = affine_transform(img, 1.3, 0, 0, 0.8, 0, 0)
    cv2.imshow("window", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    img = affine_transform(img)
    cv2.imshow("window", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
