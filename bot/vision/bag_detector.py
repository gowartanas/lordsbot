from controller.game_controller import GameController
from vision.detector import find_template


SCREENSHOT = r"C:\Users\taleh\OneDrive\Desktop\lordsbot\bot\screenshots\live_screen.png"

BAG_TEMPLATE = r"C:\Users\taleh\OneDrive\Desktop\lordsbot\bot\vision\templates\bag_real.png"


def find_bag():

    controller = GameController()

    if not controller.connect():

        print("[VISION] MuMu bağlantısı başarısız.")

        return None

    print("[VISION] Canlı ekran alınıyor...")

    if not controller.screenshot(SCREENSHOT):

        print("[VISION] Screenshot alınamadı.")

        return None

    result = find_template(
        SCREENSHOT,
        BAG_TEMPLATE,
        threshold=0.75
    )

    if result is None:

        print("[VISION] ÇANTA BULUNAMADI.")

        return None

    print()
    print("[VISION] ÇANTA BULUNDU")
    print("[VISION] Merkez:", result["center"])
    print("[VISION] Güven:", result["confidence"])

    return result["center"]


if __name__ == "__main__":

    print()
    print("=" * 50)
    print("LORDSBOT LIVE BAG DETECTOR")
    print("=" * 50)

    center = find_bag()

    print()

    if center:

        print("ÇANTA KOORDİNATI:", center)

    else:

        print("ÇANTA TESPİT EDİLEMEDİ.")
