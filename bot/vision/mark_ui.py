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

number = 1

for c in contours:

    x, y, w, h = cv2.boundingRect(c)
    area = w * h

    if (
        30 <= w <= 200
        and 30 <= h <= 150
        and area >= 1500
    ):

        x += 800
        y += 400

        cv2.rectangle(
            img,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            img,
            str(number),
            (x, max(20, y-5)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

        number += 1

out = r"C:\Users\taleh\OneDrive\Desktop\lordsbot\bot\screenshots\detected_ui.png"

cv2.imwrite(out, img)

print("HAZIR:", out)
print("Toplam aday:", number - 1)
