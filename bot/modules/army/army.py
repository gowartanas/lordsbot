from core.task import BaseTask


class ArmyTask(BaseTask):

    def __init__(self):
        super().__init__(
            name="Ordu",
            enabled=True,
            priority=9
        )

        self.settings = {}

    def configure(self, settings):
        self.settings = settings or {}

        self.enabled = bool(
            self.settings.get(
                "armyEnabled",
                False
            )
        )

    def run(self):

        auto_train = self.settings.get(
            "armyAutoTrain",
            False
        )

        auto_heal = self.settings.get(
            "armyAutoHeal",
            False
        )

        train_priority = self.settings.get(
            "armyTrainPriority",
            []
        )

        heal_limit = self.settings.get(
            "armyHealLimit",
            0
        )

        use_speedups = self.settings.get(
            "armyUseSpeedups",
            False
        )

        print("[ARMY] Ordu görevi çalıştı.")
        print(f"[ARMY] Otomatik eğitim: {auto_train}")
        print(f"[ARMY] Otomatik iyileştirme: {auto_heal}")
        print(f"[ARMY] Eğitim önceliği: {train_priority}")
        print(f"[ARMY] İyileştirme limiti: {heal_limit}")
        print(f"[ARMY] Hızlandırma kullan: {use_speedups}")