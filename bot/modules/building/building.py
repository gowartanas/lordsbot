from core.task import BaseTask


class BuildingTask(BaseTask):

    def __init__(self):
        super().__init__(
            name="Bina Geliştirme",
            enabled=True,
            priority=7
        )

        self.settings = {}

    def configure(self, settings):

        self.settings = settings or {}

        self.enabled = bool(
            self.settings.get(
                "buildingEnabled",
                False
            )
        )

    def run(self):

        auto_build = self.settings.get(
            "buildingAutoBuild",
            False
        )

        auto_upgrade = self.settings.get(
            "buildingAutoUpgrade",
            False
        )

        priority = self.settings.get(
            "buildingPriority",
            []
        )

        use_speedups = self.settings.get(
            "buildingUseSpeedups",
            False
        )

        max_level = self.settings.get(
            "buildingMaxLevel",
            0
        )

        print("[BUILDING] Bina görevi çalıştı.")
        print(f"[BUILDING] Otomatik inşa: {auto_build}")
        print(f"[BUILDING] Otomatik geliştirme: {auto_upgrade}")
        print(f"[BUILDING] Bina önceliği: {priority}")
        print(f"[BUILDING] Hızlandırma kullan: {use_speedups}")
        print(f"[BUILDING] Maksimum seviye: {max_level}")