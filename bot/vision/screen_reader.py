import os
import pytesseract
from PIL import Image

TESSERACT = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = TESSERACT

def read_screen(image_path):

    if not os.path.exists(image_path):
        return []

    image = Image.open(image_path)

    data = pytesseract.image_to_data(
        image,
        lang="eng",
        output_type=pytesseract.Output.DICT
    )

    results = []

    for i, text in enumerate(data["text"]):

        text = text.strip()

        if not text:
            continue

        try:
            confidence = float(data["conf"][i])
        except:
            confidence = 0

        if confidence < 20:
            continue

        x = data["left"][i]
        y = data["top"][i]
        w = data["width"][i]
        h = data["height"][i]

        results.append({
            "text": text,
            "confidence": round(confidence, 1),
            "center": (
                x + w // 2,
                y + h // 2
            )
        })

    return results


if __name__ == "__main__":

    screenshot = os.path.join(
        os.path.dirname(__file__),
        "..",
        "screenshots",
        "lords_mobile.png"
    )

    print()
    print("=" * 50)
    print("LORDSBOT SCREEN READER")
    print("=" * 50)

    results = read_screen(screenshot)

    for item in results:
        print(
            "[OCR]",
            item["text"],
            "| guven=",
            item["confidence"],
            "| merkez=",
            item["center"]
        )

    print()
    print("Toplam:", len(results), "metin")
