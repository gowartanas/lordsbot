import cv2
import os

IMAGE = r"C:\Users\taleh\OneDrive\Desktop\lordsbot\bot\screenshots\vision_test.png"
OUTPUT = r"C:\Users\taleh\OneDrive\Desktop\lordsbot\bot\vision\templates\selected_template.png"

image = cv2.imread(IMAGE)

if image is None:
    print("Screenshot bulunamadı!")
    exit()

print()
print("==============================================")
print(" LORDSBOT TEMPLATE SEÇİCİ")
print("==============================================")
print()
print("Fareyle seçmek istediğin bölgeyi sürükle.")
print("Sonra ENTER'a bas.")
print("ESC ile iptal edebilirsin.")
print()

x, y, w, h = cv2.selectROI(
    "Template Sec",
    image,
    False,
    False
)

cv2.destroyAllWindows()

if w == 0 or h == 0:
    print("Secim yapilmadi.")
    exit()

crop = image[y:y+h, x:x+w]

os.makedirs(
    os.path.dirname(OUTPUT),
    exist_ok=True
)

cv2.imwrite(OUTPUT, crop)

print()
print("==============================================")
print(" TEMPLATE KAYDEDILDI")
print("==============================================")
print("X:", x)
print("Y:", y)
print("Genislik:", w)
print("Yukseklik:", h)
print("Dosya:", OUTPUT)
