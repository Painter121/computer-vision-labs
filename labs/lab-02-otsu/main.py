# พัชณพงศ์ พงศ์พิมพ์ 66172110335-1
# ภูริภัทร มะลิซ้อน 66172110157-8

import cv2
import numpy as np

def convertToGray(img):
    height = len(img)
    width = len(img[0])

    gray_img = []
    for i in range(height):
        row = []
        for j in range(width):
            R = img[i][j][2]
            G = img[i][j][1]
            B = img[i][j][0]

            gray = int(0.299 * R + 0.587 * G + 0.114 * B)
            row.append(gray)
        gray_img.append(row)

    # แปลง list 2 มิติเป็น numpy array
    return np.array(gray_img, dtype=np.uint8)

def setImgZero(height,width):
    new_img = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(0)
        new_img.append(row)
    return new_img

def mapMask(img,x,y):
    neighbor = [
        img[y - 1][x - 1], img[y - 1][x], img[y - 1][x + 1],  # NW  N  NE
        img[y][x - 1],     img[y][x],     img[y][x + 1],      # W   C   E
        img[y + 1][x - 1], img[y + 1][x], img[y + 1][x + 1],  # SW  S  SE
    ]
    return neighbor

def histogram(img):
    hist = [0] * 256
    height = len(img)
    width = len(img[0])

    for y in range(height):
        for x in range(width):
            hist[ img[y][x] ] += 1
    return hist

def convertToBinary(img, T):
    height = len(img)
    width = len(img[0])
    binary_img = setImgZero(height, width)

    for y in range(height):
        for x in range(width):
            if img[y][x] >= T:
                binary_img[y][x] = 255
            else:
                binary_img[y][x] = 0

    return np.array(binary_img, dtype=np.uint8)

def otsu_threshold(img):
    hist = histogram(img)
    total = img.size

    max_value = 0
    threshold = 0

    for T in range(256):
        wB = sum(hist[0:T + 1]) / total
        wF = 1 - wB

        sumB = 0
        for i in range(0 , T + 1):
            sumB += ( i * hist[i] )

        sumF = 0
        for i in range(T + 1 , 256):
            sumF += (i * hist[i])

        if wB > 0:
            mB = sumB / (wB * total)
        else:
            mB = 0
        if wF > 0:
            mF = sumF / (wF * total)
        else:
            mF = 0

        value_between  = wB * wF * (mB - mF) ** 2

        if value_between > max_value:
            max_value = value_between
            threshold = T

    return threshold

# ----------------------- Main Function ----------------------
img = cv2.imread('./pic/leaf.jpg')

imgGray = convertToGray(img)

T = otsu_threshold(imgGray)
print(T)

imgBinary = convertToBinary(imgGray, T)

# hist = histogram(imgGray)
# print(hist)

cv2.imshow('img', img)
cv2.imshow('imgGray', imgGray)
cv2.imshow('imgBinary', imgBinary)

cv2.waitKey(0)
cv2.destroyAllWindows()

