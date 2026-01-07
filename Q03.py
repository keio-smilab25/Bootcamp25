import cv2

def BGRtoGray(img):
    gray = 0.299 * img[:, :, 2] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 0]
    return gray.astype('uint8')

def binarization(gray_img, th=128):
    gray_img = (gray_img >= th) * 255
    return gray_img.astype('uint8')

def main():
    img = cv2.imread('Gasyori100knock/Question_01_10/imori.jpg')
    img = BGRtoGray(img)
    img = binarization(img)
    cv2.imshow("window", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()