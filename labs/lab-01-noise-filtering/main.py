import sys
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

def average(img):
    height = len(img)
    width = len(img[0])
    new_img = setImgZero(height,width)

    for y in range(1, height-1):
        for x in range(1, width-1):
            neighbor = mapMask(img,x,y)

            total = 0
            for val in neighbor:
                total += int(val)
            avg = total // len(neighbor)

            new_img[y][x] = avg
    return np.array(new_img, dtype=np.uint8)


def median(img):
    height = len(img)
    width = len(img[0])
    new_img = setImgZero(height, width)

    for y in range(1, height-1):
        for x in range(1, width-1):
            neighbor = mapMask(img,x,y)

            neighbor.sort()
            median_val = neighbor[len(neighbor)//2]
            new_img[y][x] = median_val

    return np.array(new_img, dtype=np.uint8)

# ----------------------- Main Function ----------------------
imgGaussian = cv2.imread('./pic/gaussian2_0.jpg')
imgSaltPepper = cv2.imread('./pic/salt-pepper3_0.jpg')

gray_Gaussian = convertToGray(imgGaussian)
gray_SaltPepper = convertToGray(imgSaltPepper)


print('------- Image1 Size -------')
print(f'Default   : {sys.getsizeof(imgGaussian)} Bytes')
print(f'GrayScale : {sys.getsizeof(gray_Gaussian)} Bytes')
print('------- Image2 Size -------')
print(f'Default   : {sys.getsizeof(imgSaltPepper)} Bytes')
print(f'GrayScale : {sys.getsizeof(gray_SaltPepper)} Bytes')


resultAvg = average(gray_Gaussian)
for i in range(1):
    resultAvg = average(resultAvg)

resultMedian =median(gray_SaltPepper)
for i in range(1):
    resultMedian = median(resultMedian)

cv2.imshow('Gaussian', gray_Gaussian)
cv2.imshow('SaltPepper', gray_SaltPepper)
cv2.imshow('Average', resultAvg)
cv2.imshow('median', resultMedian)
cv2.waitKey(0)
cv2.destroyAllWindows()

