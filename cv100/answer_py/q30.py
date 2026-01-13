import cv2
import numpy as np

def rotate_origin_nn(img: np.ndarray, deg: float) -> np.ndarray:
    h, w, c = img.shape
    out = np.zeros((h, w, c), dtype=np.uint8)

    rad = np.deg2rad(deg)
    cos_a = float(np.cos(rad))
    sin_a = float(np.sin(rad))

    for y_out in range(h):
        for x_out in range(w):
            x_src = cos_a * x_out - sin_a * y_out
            y_src = sin_a * x_out + cos_a * y_out

            xi = int(round(x_src))
            yi = int(round(y_src))

            if 0 <= xi < w and 0 <= yi < h:
                out[y_out, x_out, :] = img[yi, xi, :]

    return out

def rotate_center_nn(img: np.ndarray, deg: float) -> np.ndarray:
    h, w, c = img.shape
    out = np.zeros((h, w, c), dtype=np.uint8)

    rad = np.deg2rad(deg)
    cos_a = float(np.cos(rad))
    sin_a = float(np.sin(rad))

    cx = (w - 1) / 2.0
    cy = (h - 1) / 2.0

    for y_out in range(h):
        for x_out in range(w):
            dx = x_out - cx
            dy = y_out - cy

            x_src = cos_a * dx - sin_a * dy + cx
            y_src = sin_a * dx + cos_a * dy + cy

            xi = int(round(x_src))
            yi = int(round(y_src))

            if 0 <= xi < w and 0 <= yi < h:
                out[y_out, x_out, :] = img[yi, xi, :]

    return out

if __name__ == "__main__":
    img = cv2.imread("../../../Gasyori100knock/Question_21_30/imori.jpg")
    if img is None:
        raise FileNotFoundError("../../../Gasyori100knock/Question_21_30/imori.jpg")

    out1 = rotate_origin_nn(img, deg=30)
    out2 = rotate_center_nn(img, deg=30)

    cv2.imwrite("../answers_image/answer_30_1.jpg", out1)
    print("saved: ../answers_image/answer_30_1.jpg")
    cv2.imwrite("../answers_image/answer_30_2.jpg", out2)
    print("saved: ../answers_image/answer_30_2.jpg")
