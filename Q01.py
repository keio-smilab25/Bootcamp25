import cv2

def RGBtoBGR(img):
    r = img[:, :, 0].copy()
    img[:, :, 0] = img[:, :, 2]
    img[:, :, 2] = r
    return img

def main():
    img = cv2.imread('Gasyori100knock/Question_01_10/imori.jpg')
    img = RGBtoBGR(img)
    cv2.imshow("window", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()