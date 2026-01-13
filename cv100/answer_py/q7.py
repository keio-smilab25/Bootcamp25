import cv2
import numpy as np

def average_pooling(img: np.ndarray, pool_h: int = 8, pool_w: int = 8) -> np.ndarray:
    h, w, c = img.shape
    out = img.copy().astype(np.float32)

    for y in range(0, h, pool_h):
        for x in range(0, w, pool_w):
            block = out[y:y + pool_h, x:x + pool_w, :]
            mean_val = block.mean(axis=(0, 1), keepdims=True)
            out[y:y + pool_h, x:x + pool_w, :] = mean_val

    return np.clip(out, 0, 255).astype(np.uint8)

if __name__ == "__main__":
    img = cv2.imread("../../../Gasyori100knock/assets/imori.jpg")
    if img is None:
        raise FileNotFoundError("imori.jpg")

    out = average_pooling(img, pool_h=8, pool_w=8)

    cv2.imwrite("../answers_image/answer_7.jpg", out)
    print("saved: ../answers_image/answer_7.jpg")