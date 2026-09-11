import cv2
import numpy as np

def prewitt_edge(image_bgr,T):
    gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

    # Kernel ของ Prewitt (3x3)
    kernel_x = np.array([
        [ 1,  0, -1],
        [ 1,  0, -1],
        [ 1,  0, -1]
    ], dtype=np.float32)

    kernel_y = np.array([
        [ 1,  1,  1],
        [ 0,  0,  0],
        [-1, -1, -1]
    ], dtype=np.float32)

    gx = cv2.filter2D(gray, cv2.CV_32F, kernel_x)
    gy = cv2.filter2D(gray, cv2.CV_32F, kernel_y)

    edge = np.sqrt(gx**2 + gy**2)
    edge = np.clip(edge, 0, 255).astype(np.uint8)

    # ==========================================
    # ตัด Noise ทิ้งด้วย Threshold
    # ==========================================
    # - ถ้าเส้นติดกัน ต้องเพิ่มค่า T นี้เป็น 120-130
    _, edge_binary = cv2.threshold(edge, T, 255, cv2.THRESH_BINARY)

    return edge_binary