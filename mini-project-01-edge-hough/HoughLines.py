import cv2
import numpy as np

from Robert import roberts_edge
from Prewitt import prewitt_edge
from Sobel import sobel_edge
from Canny import canny_edge

# =========================
#  อ่าน + resize ภาพ
# =========================
img = cv2.imread("./pic/l3.jpg")
h, w = img.shape[:2]
new_w = 300
scale = new_w / w
new_h = int(h * scale)
img = cv2.resize(img, (new_w, new_h))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# =========================
#  Edge 4 วิธี
# =========================
edges_dict = {
    "Roberts": roberts_edge(img,100),
    "Prewitt": prewitt_edge(img,100),
    "Sobel":   sobel_edge(img,100),
    "Canny":   canny_edge(img)
}

# =========================
# วาดเส้นด้วย HoughLines
# =========================
def draw_hough_lines_p(edge_img, src_img, max_lines=10):
    result = src_img.copy()

    lines = cv2.HoughLinesP(
        edge_img,
        rho=1,
        theta=np.pi / 180,
        threshold=80,
        minLineLength=60,   # ปรับตามภาพ
        maxLineGap=10
    )
    count = 0
    if lines is not None:
        count = len(lines)
        for i in range(min(len(lines), max_lines)):
            x1, y1, x2, y2 = lines[i][0]
            cv2.line(result, (x1, y1), (x2, y2), (0, 0, 255), 2)

    return result, count

# =========================
# แสดงผล
# =========================
for name, edge in edges_dict.items():
    hough_img, line_count = draw_hough_lines_p(edge, img)

    print(f"{name}: detected {line_count} lines")

    cv2.imshow(f"{name} Edge", edge)
    cv2.imshow(f"{name} + HoughP", hough_img)

cv2.waitKey(0)
cv2.destroyAllWindows()