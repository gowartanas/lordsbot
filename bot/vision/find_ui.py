import cv2

img = cv2.imread(
    r"C:\Users\taleh\OneDrive\Desktop\lordsbot\bot\screenshots\vision_test_3.png"
)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Sağ-alt oyun arayüzü
roi = hsv[450:720, 800:1280]

# Parlak / doygun UI bölgelerini bul
mask = cv2.inRange(
    roi,
    (0, 80, 100),
    (179, 255, 255)
)

contours, _ = cv2.findContours(
    mask,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

print()
print("=== SAĞ ALT ADAYLARI ===")

found = 0

for c in contours:

    x, y, w, h = cv2.boundingRect(c)

    if 20 <= w <= 200 and 20 <= h <= 150:

        print(
            "X:", x + 800,
            "Y:", y + 450,
            "W:", w,
            "H:", h
        )

        found += 1

print()
print("Toplam aday:", found)
