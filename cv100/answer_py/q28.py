import cv2
import numpy as np

def affine_translate(img: np.ndarray, tx: int = 30, ty: int = -30) -> np.ndarray:
    h, w, c = img.shape
    out = np.zeros((h, w, c), dtype=np.uint8)
    for y_out in range(h):
        y_src = y_out - ty
        if y_src < 0 or y_src >= h:
            continue
        for x_out in range(w):
            x_src = x_out - tx
            if x_src < 0 or x_src >= w:
                continue
            out[y_out, x_out, :] = img[y_src, x_src, :]

    return out

if __name__ == "__main__":
    img = cv2.imread("../../../Gasyori100knock/Question_21_30/imori.jpg")
    if img is None:
        raise FileNotFoundError("../../../Gasyori100knock/Question_21_30/imori.jpg")

    out = affine_translate(img, tx=30, ty=-30)

    cv2.imwrite("../answers_image/answer_28.jpg", out)
    print("saved: ../answers_image/answer_28.jpg")