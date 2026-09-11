# Computer Vision Coursework

รวมแบบฝึกหัดและการประมวลผลภาพดิจิทัลในรายวิชา Computer Vision ครอบคลุมการคำนวณคุณลักษณะภาพ, การบีบอัดข้อมูล และการวิเคราะห์ภาพดิจิทัล

---

## 1. Texture Segmentation — GLCM (Gray-Level Co-occurrence Matrix)

การสกัดคุณลักษณะเนื้อสัมผัสของภาพโดยการสร้างเมทริกซ์การเกิดร่วมระดับสีเทา (GLCM) จากพิกเซลในทิศทางต่าง ๆ พร้อมคำนวณค่า Contrast, Similarity และ Dissimilarity เพื่อใช้ในการแบ่งส่วนภาพ

![ตัวอย่างคำตอบ GLCM](texture-segmentation/preview.png)

[ดูเอกสารและผลการคำนวณฉบับเต็ม (10 หน้า)](texture-segmentation/answers.pdf)

---

## 2. Huffman Coding

การบีบอัดข้อมูลภาพแบบไม่สูญเสียรายละเอียด (Lossless Data Compression) โดยคำนวณความน่าจะเป็นของระดับความสว่างพิกเซล สร้าง Huffman Tree กำหนดรหัสบิต พร้อมทั้งคำนวณ Average Code Length และ Compression Ratio

![ตัวอย่างคำตอบ Huffman Coding](huffman-coding/preview.png)

[ดูเอกสารและขั้นตอนการเข้ารหัสฉบับเต็ม (5 หน้า)](huffman-coding/answers.pdf)

---

## 3. Connected-Component Labeling

อัลกอริทึมการระบุและจัดกลุ่มวัตถุในภาพไบนารี (Binary Image) โดยการกำหนด Label ให้แก่พิกเซลที่เชื่อมต่อกัน (Connected Pixels) และรวมกลุ่มเพื่อแยกแยะชิ้นส่วนวัตถุในภาพ

![คำตอบ Connected-Component Labeling](connected-component-labeling/preview.png)

[ดูเอกสารและผลลัพธ์ขนาดเต็ม](connected-component-labeling/answers.pdf)


## 4. Python Labs

| งาน | สิ่งที่ทำ |
|---|---|
| [Lab 1 — Noise Filtering](labs/lab-01-noise-filtering/main.py) | แปลง grayscale และเขียนตัวกรอง Average/Median เพื่อลด Gaussian กับ Salt-and-pepper noise |
| [Lab 2 — Otsu Threshold](labs/lab-02-otsu/main.py) | คำนวณ histogram หา threshold และแปลงภาพเป็น binary |
| [Mini Project 1 — Edge & Hough](mini-project-01-edge-hough/README.md) | เปรียบเทียบ Roberts, Prewitt, Sobel, Canny และตรวจเส้น/วงกลมด้วย Hough Transform |

ใช้ Python 3.10 แล้วติดตั้งไลบรารี:

```sh
pip install -r requirements.txt
```

เข้าโฟลเดอร์ lab ที่ต้องการก่อนรัน `python main.py` เพื่อให้โปรแกรมอ่านรูปใน `pic` ได้ ส่วน mini project มีวิธีเปิดแยกอยู่ในโฟลเดอร์งาน

Lab 2 ทำร่วมกับ พัชณพงศ์ พงศ์พิมพ์

## 5. Mini Project 2 — Scene Classification

[โปรเจกต์จำแนกฉากด้วย EfficientNetB0](https://github.com/Painter121/computer-vision-mini-project-scene-classification) มีโมเดลที่ฝึกแล้วและหน้าเว็บ Gradio สำหรับอัปโหลดภาพ
