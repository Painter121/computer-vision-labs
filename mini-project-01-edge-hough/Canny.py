import cv2

def canny_edge(image_bgr, blur_ksize=(5, 5)):
    gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    # ลด noise
    blur = cv2.GaussianBlur(gray, blur_ksize, 0)
    # Auto threshold
    sigma = blur.std()
    lower = max(20, int(0.66 * sigma))
    upper = min(200, int(1.33 * sigma))

    edges = cv2.Canny(blur, lower, upper)

    return edges