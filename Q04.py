import cv2

def BGRtoGray(img):
    gray = 0.299 * img[:, :, 2] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 0]
    return gray.astype('uint8')

def binarization(gray_img, th=128):
    gray_img = (gray_img >= th) * 255
    return gray_img.astype('uint8')

def ootsu_binarization(gray_img, th=128):
    best_th = th
    max_sb_2 = -1
    for t in range(256):
        w0 = (gray_img < t).sum()
        w1 = (gray_img >= t).sum()
        if w0 == 0 or w1 == 0:
            continue
        m0 = gray_img[gray_img < t].mean() if w0 > 0 else 0
        m1 = gray_img[gray_img >= t].mean() if w1 > 0 else 0
        sb_2 = w0 * w1 * (m0 - m1) ** 2
        if sb_2 > max_sb_2:
            max_sb_2 = sb_2
            best_th = t
    return best_th

def main():
    img = cv2.imread('Gasyori100knock/Question_01_10/imori.jpg')
    img = BGRtoGray(img)
    img = binarization(img, ootsu_binarization(img))
    cv2.imshow("window", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()