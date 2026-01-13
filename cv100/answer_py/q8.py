import cv2
import numpy as np

def max_pooling(img: np.ndarray, pool: int = 8) -> np.ndarray:
    h, w, c = img.shape
    out = img.copy().astype(np.float32)

    for y in range(0, h, pool):
        for x in range(0, w, pool):
            block = out[y:y + pool, x:x + pool, :]
            max_val = block.max(axis=(0, 1), keepdims=True)
            out[y:y + pool, x:x + pool, :] = max_val

    return np.clip(out, 0, 255).astype(np.uint8)

if __name__ == "__main__":
    img = cv2.imread("../../../Gasyori100knock/assets/imori.jpg")
    if img is None:
        raise FileNotFoundError("../../../Gasyori100knock/assets/imori.jpg")

    out = max_pooling(img, pool=8)

    cv2.imwrite("../answers_image/answer_8.jpg", out)
    print("saved: ../answers_image/answer_8.jpg")