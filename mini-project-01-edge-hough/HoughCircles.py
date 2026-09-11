import cv2
import numpy as np

from Robert import roberts_edge
from Prewitt import prewitt_edge
from Sobel import sobel_edge
from Canny import canny_edge

# =========================
#  อ่าน + resize ภาพ
# =========================
img = cv2.imread("./pic/c3.jpg")
h, w = img.shape[:2]
new_w = 600
scale = new_w / w
new_h = int(h * scale)
img = cv2.resize(img, (new_w, new_h))

# =========================
#  Edge 4 วิธี
# =========================
edges_dict = {
    "Roberts": roberts_edge(img, 30),
    "Prewitt": prewitt_edge(img, 100),
    "Sobel":   sobel_edge(img,100),
    "Canny":   canny_edge(img)
}

# =========================
# GUI Trackbar
# =========================
cv2.namedWindow("Hough Control", cv2.WINDOW_NORMAL)
def nothing(x):
    pass

cv2.createTrackbar("dp x10",  "Hough Control", 10, 40, nothing)
cv2.createTrackbar("minDist","Hough Control", 10, 300, nothing)
cv2.createTrackbar("param1", "Hough Control", 50, 400, nothing)
cv2.createTrackbar("param2", "Hough Control", 40, 400, nothing)
cv2.createTrackbar("minR",   "Hough Control", 10, 300, nothing)
cv2.createTrackbar("maxR",   "Hough Control", 50, 400, nothing)

# =========================
# Loop แสดงผล รวมภาพแล้วใส่ใน Hough Control
# =========================
while True:
    # อ่านค่าจาก Trackbar
    dp = max(0.1, cv2.getTrackbarPos("dp x10", "Hough Control") / 10)
    minDist = max(1, cv2.getTrackbarPos("minDist", "Hough Control"))
    param1 = max(1, cv2.getTrackbarPos("param1", "Hough Control"))
    param2 = max(1, cv2.getTrackbarPos("param2", "Hough Control"))
    minR = cv2.getTrackbarPos("minR", "Hough Control")
    maxR = cv2.getTrackbarPos("maxR", "Hough Control")

    results_list = []  # ลิสต์สำหรับเก็บภาพผลลัพธ์ทั้ง 4

    for name, edge in edges_dict.items():
        circle_count = 0
        result = img.copy()
        # Blur เพื่อลด Noise ก่อนเข้า Hough
        gray = cv2.GaussianBlur(edge, (9, 9), 1.5)

        if dp > 0 and minDist > 0 and maxR > minR:
            circles = cv2.HoughCircles(
                gray,
                cv2.HOUGH_GRADIENT,
                dp=dp,
                minDist=minDist,
                param1=param1,
                param2=param2,
                minRadius=minR,
                maxRadius=maxR
            )

            if circles is not None:
                circles = np.uint16(np.around(circles))
                circle_count = len(circles[0])
                for x, y, r in circles[0]:
                    cv2.circle(result, (x, y), r, (0, 255, 0), 2)
                    cv2.circle(result, (x, y), 2, (0, 0, 255), 3)

        # เขียนชื่อ  แปะลงบนภาพ และตัวนับ
        cv2.putText(
            result,
            f"{name} | circles: {circle_count}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

        results_list.append(result)

    # --- รวมภาพ 4 ภาพ เป็น Grid 2x2 ---
    # แถวบน: Roberts + Prewitt
    top_row = np.hstack((results_list[0], results_list[1]))
    # แถวล่าง: Sobel + Canny
    bottom_row = np.hstack((results_list[2], results_list[3]))
    # รวมบนกับล่าง
    combined_img = np.vstack((top_row, bottom_row))

    cv2.imshow("Hough Control", combined_img)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

cv2.destroyAllWindows()