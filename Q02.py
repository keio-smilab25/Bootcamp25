import cv2

def BGRtoGray(img):
    gray = 0.299 * img[:, :, 2] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 0]
    return gray.astype('uint8')

def main():
    img = cv2.imread('Gasyori100knock/Question_01_10/imori.jpg')
    gray_img = BGRtoGray(img)
    cv2.imshow("window", gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()