import cv2
import numpy as np

def median_filter_3x3(img: np.ndarray) -> np.ndarray:
    h, w, c = img.shape
    out = np.zeros((h, w, c), dtype=np.uint8)

    pad = 1
    padded = np.pad(img, ((pad, pad), (pad, pad), (0, 0)),
                    mode="constant", constant_values=0)

    for y in range(h):
        for x in range(w):
            patch = padded[y:y + 3, x:x + 3, :]
            out[y, x, 0] = np.median(patch[:, :, 0])
            out[y, x, 1] = np.median(patch[:, :, 1])
            out[y, x, 2] = np.median(patch[:, :, 2])

    return out

if __name__ == "__main__":
    img = cv2.imread("../../../Gasyori100knock/Question_01_10/imori_noise.jpg")
    if img is None:
        raise FileNotFoundError("../../../Gasyori100knock/Question_01_10/imori_noise.jpg")

    out = median_filter_3x3(img)

    cv2.imwrite("../answers_image/answer_10.jpg", out)
    print("saved: ../answers_image/answer_10.jpg")