import subprocess
import time


ADB = r"C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe"


class GameController:

    def __init__(self):

        self.device = None
        self.connected = False

    def connect(self, device=None):

        self.device = device

        try:

            result = subprocess.run(
                [ADB, "devices"],
                capture_output=True,
                text=True,
                timeout=10
            )

            if result.returncode != 0:
                return False

            lines = result.stdout.splitlines()

            devices = []

            for line in lines:

                line = line.strip()

                if (
                    line
                    and not line.startswith("List of devices")
                    and "\tdevice" in line
                ):
                    devices.append(
                        line.split("\t")[0]
                    )

            if not devices:
                self.connected = False
                return False

            if self.device is None:
                self.device = devices[0]

            self.connected = True

            print(
                f"[CONTROLLER] Cihaz bağlandı: "
                f"{self.device}"
            )

            return True

        except Exception as exc:

            print(
                "[CONTROLLER] Bağlantı hatası:",
                exc
            )

            self.connected = False

            return False

    def disconnect(self):

        self.connected = False
        self.device = None

        print(
            "[CONTROLLER] Cihaz bağlantısı kapatıldı."
        )

    def tap(self, x, y):

        if not self.connected:
            return False

        try:

            subprocess.run(
                [
                    ADB,
                    "-s",
                    self.device,
                    "shell",
                    "input",
                    "tap",
                    str(x),
                    str(y)
                ],
                check=True,
                timeout=10
            )

            print(
                f"[CONTROLLER] TAP: {x}, {y}"
            )

            return True

        except Exception as exc:

            print(
                "[CONTROLLER] TAP hatası:",
                exc
            )

            return False

    def swipe(
        self,
        x1,
        y1,
        x2,
        y2,
        duration=500
    ):

        if not self.connected:
            return False

        try:

            subprocess.run(
                [
                    ADB,
                    "-s",
                    self.device,
                    "shell",
                    "input",
                    "swipe",
                    str(x1),
                    str(y1),
                    str(x2),
                    str(y2),
                    str(duration)
                ],
                check=True,
                timeout=10
            )

            print(
                f"[CONTROLLER] SWIPE: "
                f"{x1},{y1} -> {x2},{y2}"
            )

            return True

        except Exception as exc:

            print(
                "[CONTROLLER] SWIPE hatası:",
                exc
            )

            return False

    def press_back(self):

        if not self.connected:
            return False

        try:

            subprocess.run(
                [
                    ADB,
                    "-s",
                    self.device,
                    "shell",
                    "input",
                    "keyevent",
                    "4"
                ],
                check=True,
                timeout=10
            )

            print(
                "[CONTROLLER] BACK"
            )

            return True

        except Exception as exc:

            print(
                "[CONTROLLER] BACK hatası:",
                exc
            )

            return False

    def screenshot(self, output_path):

        if not self.connected:
            return False

        try:

            with open(
                output_path,
                "wb"
            ) as image_file:

                result = subprocess.run(
                    [
                        ADB,
                        "-s",
                        self.device,
                        "exec-out",
                        "screencap",
                        "-p"
                    ],
                    stdout=image_file,
                    timeout=20
                )

            if result.returncode != 0:
                return False

            print(
                f"[CONTROLLER] Screenshot: "
                f"{output_path}"
            )

            return True

        except Exception as exc:

            print(
                "[CONTROLLER] Screenshot hatası:",
                exc
            )

            return False

    def wait(self, seconds):

        time.sleep(seconds)