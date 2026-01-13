import cv2
import numpy as np


def affine(img, a, b, c, d, tx, ty):
    H, W, C = img.shape

    tmp = np.zeros((H + 2, W + 2, C), dtype=np.float32)
    tmp[1:H + 1, 1:W + 1] = img

    H_new = int(np.round(H * d))
    W_new = int(np.round(W * a))
    out = np.zeros((H_new + 1, W_new + 1, C), dtype=np.float32)

    x_new = np.tile(np.arange(W_new), (H_new, 1))
    y_new = np.arange(H_new).repeat(W_new).reshape(H_new, -1)

    adbc = a * d - b * c
    x = np.round((d * x_new - b * y_new) / adbc).astype(int) - tx + 1
    y = np.round((-c * x_new + a * y_new) / adbc).astype(int) - ty + 1

    x = np.minimum(np.maximum(x, 0), W + 1).astype(int)
    y = np.minimum(np.maximum(y, 0), H + 1).astype(int)

    out[y_new, x_new] = tmp[y, x]

    out = out[:H_new, :W_new].astype(np.uint8)
    return out


if __name__ == "__main__":
    img = cv2.imread("../../../Gasyori100knock/Question_21_30/imori.jpg").astype(np.float32)
    if img is None:
        raise FileNotFoundError("../../../Gasyori100knock/Question_21_30/imori.jpg")

    out1 = affine(img, a=1.3, b=0, c=0, d=0.8, tx=0, ty=0)
    out2 = affine(img, a=1.3, b=0, c=0, d=0.8, tx=30, ty=-30)

    cv2.imwrite("../answers_image/answer_29_1.jpg", out1)
    print("saved: ../answers_image/answer_29_1.jpg")

    cv2.imwrite("../answers_image/answer_29_2.jpg", out2)
    print("saved: ../answers_image/answer_29_2.jpg")