import cv2

def sobel_edge(image_bgr,T, ksize=3):
    gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

    # เพราะตัว Kernel มันมีการคำนวณแบบ Gaussian ในตัว
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=ksize)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=ksize)

    sobel = cv2.magnitude(sobel_x, sobel_y)
    sobel = cv2.convertScaleAbs(sobel) # ตอนนี้เป็น Grayscale (0-255)

    # ลองเริ่มที่ 100 หรือ 120  ถ้าเส้นหายให้ลดลงมา
    _, sobel_binary = cv2.threshold(sobel, T, 255, cv2.THRESH_BINARY)

    return sobel_binary