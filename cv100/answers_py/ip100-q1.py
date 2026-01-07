import cv2

def BGRtoRGB(img):
    red = img[:, :, 2].copy()
    green = img[:, :, 1].copy()
    blue = img[:, :, 0].copy()

    img[:, :, 0] = red
    img[:, :, 1] = green
    img[:, :, 2] = blue

    return img


img = cv2.imread("../../Gasyori100knock/Question_01_10/imori.jpg")

img_rgb = BGRtoRGB(img)
cv2.imwrite("../answers_image/answer_1.jpg", img_rgb)