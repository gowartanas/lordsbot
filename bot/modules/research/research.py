from core.task import BaseTask


class ResearchTask(BaseTask):

    def __init__(self):
        super().__init__(
            name="Araştırma",
            enabled=True,
            priority=8
        )

        self.settings = {}

    def configure(self, settings):
        self.settings = settings or {}

        self.enabled = bool(
            self.settings.get(
                "researchEnabled",
                False
            )
        )

    def run(self):

        auto_research = self.settings.get(
            "researchAutoStart",
            False
        )

        priority = self.settings.get(
            "researchPriority",
            []
        )

        use_speedups = self.settings.get(
            "researchUseSpeedups",
            False
        )

        max_level = self.settings.get(
            "researchMaxLevel",
            0
        )

        print("[RESEARCH] Araştırma görevi çalıştı.")
        print(f"[RESEARCH] Otomatik başlat: {auto_research}")
        print(f"[RESEARCH] Araştırma önceliği: {priority}")
        print(f"[RESEARCH] Hızlandırma kullan: {use_speedups}")
        print(f"[RESEARCH] Maksimum seviye: {max_level}")