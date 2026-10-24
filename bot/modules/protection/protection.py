from core.task import BaseTask


class ProtectionTask(BaseTask):

    def __init__(self):
        super().__init__(
            name="Koruma",
            enabled=True,
            priority=1
        )

        self.settings = {}

    def configure(self, settings):
        self.settings = settings or {}

        self.enabled = bool(
            self.settings.get("shieldEnabled", True)
        )

    def run(self):
        duration = self.settings.get(
            "shieldDuration",
            "8 saat"
        )

        longest = self.settings.get(
            "longestShield",
            False
        )

        always = self.settings.get(
            "alwaysShield",
            False
        )

        before_expire = self.settings.get(
            "shieldBeforeExpire",
            False
        )

        threat_action = self.settings.get(
            "threatAction",
            "shield"
        )

        minimum_time = self.settings.get(
            "minimumShieldTime",
            30
        )

        protect_gathering = self.settings.get(
            "protectGathering",
            True
        )

        print("[PROTECTION] Koruma görevi çalıştı.")

        print(
            f"[PROTECTION] Süre: {duration} | "
            f"En uzun: {longest}"
        )

        print(
            f"[PROTECTION] Sürekli: {always} | "
            f"Yenile: {before_expire}"
        )

        print(
            f"[PROTECTION] Tehdit: {threat_action} | "
            f"Minimum: {minimum_time}"
        )

        print(
            f"[PROTECTION] Toplama koruması: "
            f"{protect_gathering}"
        )