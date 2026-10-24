from core.task import BaseTask


class GatheringTask(BaseTask):

    def __init__(self):
        super().__init__(
            name="Kaynak Toplama",
            enabled=True,
            priority=1
        )

        self.settings = {}

    def configure(self, settings):
        self.settings = settings or {}

        # Dashboard'daki gatherEnabled ayarı
        self.enabled = bool(
            self.settings.get("gatherEnabled", True)
        )

    def run(self):
        max_armies = self.settings.get(
            "maxGatherArmies", 1
        )

        spare_armies = self.settings.get(
            "spareGatherArmies", 0
        )

        regather = self.settings.get(
            "regather", False
        )

        priority = self.settings.get(
            "resourcePriority",
            ["ore", "stone", "gold", "wood", "food"]
        )

        print(
            "[GATHERING] Kaynak toplama görevi çalıştı."
        )

        print(
            f"[GATHERING] Ordu: {max_armies} | "
            f"Boşta: {spare_armies}"
        )

        print(
            f"[GATHERING] Yeniden toplama: {regather}"
        )

        print(
            f"[GATHERING] Kaynak önceliği: {priority}"
        )