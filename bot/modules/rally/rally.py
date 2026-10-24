from core.task import BaseTask


class RallyTask(BaseTask):

    def __init__(self):
        super().__init__(
            name="Rally",
            enabled=True,
            priority=5
        )

        self.settings = {}

    def configure(self, settings):

        self.settings = settings or {}

        self.enabled = bool(
            self.settings.get(
                "rallyEnabled",
                False
            )
        )

    def run(self):

        auto_join = self.settings.get(
            "rallyAutoJoin",
            False
        )

        auto_create = self.settings.get(
            "rallyAutoCreate",
            False
        )

        rally_type = self.settings.get(
            "rallyType",
            "monster"
        )

        max_rallies = self.settings.get(
            "rallyMaxRallies",
            3
        )

        min_troops = self.settings.get(
            "rallyMinTroops",
            0
        )

        use_speedups = self.settings.get(
            "rallyUseSpeedups",
            False
        )

        print("[RALLY] Rally görevi çalıştı.")
        print(f"[RALLY] Otomatik katıl: {auto_join}")
        print(f"[RALLY] Otomatik oluştur: {auto_create}")
        print(f"[RALLY] Rally tipi: {rally_type}")
        print(f"[RALLY] Maksimum rally: {max_rallies}")
        print(f"[RALLY] Minimum asker: {min_troops}")
        print(f"[RALLY] Hızlandırma kullan: {use_speedups}")