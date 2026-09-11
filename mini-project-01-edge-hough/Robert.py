import cv2
import numpy as np

def roberts_edge(image_bgr ,T):
    # แปลงเป็น Gray
    gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

    kernel_x = np.array([[1, 0],
                                [0, -1]], dtype=np.float32)

    kernel_y = np.array([[0, 1],
                                [-1, 0]], dtype=np.float32)

    gx = cv2.filter2D(gray, cv2.CV_32F, kernel_x)
    gy = cv2.filter2D(gray, cv2.CV_32F, kernel_y)

    edge = np.sqrt(gx ** 2 + gy ** 2)
    edge = np.clip(edge, 0, 255).astype(np.uint8)

    #  Threshold:
    # - ถ้าต่ำกว่า 100 ให้เป็น 0 (สีดำ -> ตัดทิ้ง)
    # - ถ้าเกิน 100 ให้เป็น 255 (สีขาว -> เก็บไว้)
    # ถ้าเส้นหายให้ลดลง  ถ้าขยะเยอะให้เพิ่มขึ้น
    _, edge_binary = cv2.threshold(edge, T, 255, cv2.THRESH_BINARY)

    return edge_binary