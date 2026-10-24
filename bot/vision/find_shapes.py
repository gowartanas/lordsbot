import cv2

img = cv2.imread(
    r"C:\Users\taleh\OneDrive\Desktop\lordsbot\bot\screenshots\vision_test_3.png"
)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

roi = gray[400:720, 800:1280]

blur = cv2.GaussianBlur(
    roi,
    (5, 5),
    0
)

edges = cv2.Canny(
    blur,
    50,
    150
)

contours, _ = cv2.findContours(
    edges,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

print()
print("=== ŞEKİL ADAYLARI ===")

found = 0

for c in contours:

    x, y, w, h = cv2.boundingRect(c)

    area = w * h

    if (
        30 <= w <= 200
        and 30 <= h <= 150
        and area >= 1500
    ):

        print(
            f"X:{x+800} "
            f"Y:{y+400} "
            f"W:{w} "
            f"H:{h} "
            f"AREA:{area}"
        )

        found += 1

print()
print("Toplam:", found)
