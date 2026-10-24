import cv2
import os


def find_template(
    screenshot_path,
    template_path,
    threshold=0.80
):

    if not os.path.exists(screenshot_path):
        print("[DETECTOR] Screenshot bulunamadı.")
        return None

    if not os.path.exists(template_path):
        print("[DETECTOR] Template bulunamadı.")
        return None

    screen = cv2.imread(screenshot_path)
    template = cv2.imread(template_path)

    if screen is None:
        print("[DETECTOR] Screenshot okunamadı.")
        return None

    if template is None:
        print("[DETECTOR] Template okunamadı.")
        return None

    screen_gray = cv2.cvtColor(
        screen,
        cv2.COLOR_BGR2GRAY
    )

    template_gray = cv2.cvtColor(
        template,
        cv2.COLOR_BGR2GRAY
    )

    result = cv2.matchTemplate(
        screen_gray,
        template_gray,
        cv2.TM_CCOEFF_NORMED
    )

    _, max_value, _, max_location = cv2.minMaxLoc(
        result
    )

    if max_value < threshold:

        print(
            f"[DETECTOR] Bulunamadı | "
            f"güven={max_value:.3f}"
        )

        return None

    h, w = template_gray.shape

    x = max_location[0]
    y = max_location[1]

    center_x = x + w // 2
    center_y = y + h // 2

    result_data = {
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "center": (
            center_x,
            center_y
        ),
        "confidence": round(
            float(max_value),
            3
        )
    }

    print(
        "[DETECTOR] BULUNDU:",
        result_data
    )

    return result_data
