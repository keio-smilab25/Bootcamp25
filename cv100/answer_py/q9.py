import cv2
import numpy as np

def gaussian_filter_3x3(img: np.ndarray) -> np.ndarray:
    k = (1.0 / 16.0) * np.array(
        [[1, 2, 1],
         [2, 4, 2],
         [1, 2, 1]], dtype=np.float32
    )

    h, w, c = img.shape
    out = np.zeros((h, w, c), dtype=np.float32)

    pad = 1
    padded = np.pad(img.astype(np.float32),
                    ((pad, pad), (pad, pad), (0, 0)),
                    mode="constant", constant_values=0)

    for y in range(h):
        for x in range(w):
            patch = padded[y:y + 3, x:x + 3, :]
            out[y, x, :] = (patch * k[:, :, None]).sum(axis=(0, 1))

    return np.clip(out, 0, 255).astype(np.uint8)

if __name__ == "__main__":
    img = cv2.imread("../../../Gasyori100knock/Question_01_10/imori_noise.jpg")
    if img is None:
        raise FileNotFoundError("../../../Gasyori100knock/Question_01_10/imori_noise.jpg")

    out = gaussian_filter_3x3(img)

    cv2.imwrite("../answers_image/answer_9.jpg", out)
    print("saved: ../answers_image/answer_9.jpg")