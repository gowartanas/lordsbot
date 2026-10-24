from core.task import BaseTask


class FamiliarsTask(BaseTask):

    def __init__(self):
        super().__init__(
            name="Familiars",
            enabled=True,
            priority=12
        )

        self.settings = {}

    def configure(self, settings):
        self.settings = settings or {}

        self.enabled = bool(
            self.settings.get(
                "familiarsEnabled",
                False
            )
        )

    def run(self):

        auto_train = self.settings.get(
            "familiarsAutoTrain",
            False
        )

        auto_upgrade = self.settings.get(
            "familiarsAutoUpgrade",
            False
        )

        priority = self.settings.get(
            "familiarsPriority",
            []
        )

        use_speedups = self.settings.get(
            "familiarsUseSpeedups",
            False
        )

        print("[FAMILIARS] Familiar görevi çalıştı.")
        print(f"[FAMILIARS] Otomatik eğitim: {auto_train}")
        print(f"[FAMILIARS] Otomatik geliştirme: {auto_upgrade}")
        print(f"[FAMILIARS] Familiar önceliği: {priority}")
        print(f"[FAMILIARS] Hızlandırma kullan: {use_speedups}")