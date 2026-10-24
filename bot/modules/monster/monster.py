from core.task import BaseTask


class MonsterTask(BaseTask):

    def __init__(self):
        super().__init__(
            name="Canavar Avı",
            enabled=True,
            priority=4
        )

        self.settings = {}

    def configure(self, settings):

        self.settings = settings or {}

        self.enabled = bool(
            self.settings.get(
                "monsterEnabled",
                False
            )
        )

    def run(self):

        auto_hunt = self.settings.get(
            "monsterAutoHunt",
            False
        )

        monster_level = self.settings.get(
            "monsterLevel",
            1
        )

        max_attempts = self.settings.get(
            "monsterMaxAttempts",
            5
        )

        energy_limit = self.settings.get(
            "monsterEnergyLimit",
            0
        )

        use_energy = self.settings.get(
            "monsterUseEnergy",
            False
        )

        use_speedups = self.settings.get(
            "monsterUseSpeedups",
            False
        )

        preferred_monsters = self.settings.get(
            "monsterPriority",
            []
        )

        print(
            "[MONSTER] Canavar avı görevi çalıştı."
        )

        print(
            f"[MONSTER] Otomatik av: {auto_hunt}"
        )

        print(
            f"[MONSTER] Canavar seviyesi: "
            f"{monster_level}"
        )

        print(
            f"[MONSTER] Maksimum deneme: "
            f"{max_attempts}"
        )

        print(
            f"[MONSTER] Enerji limiti: "
            f"{energy_limit}"
        )

        print(
            f"[MONSTER] Enerji kullan: "
            f"{use_energy}"
        )

        print(
            f"[MONSTER] Hızlandırma kullan: "
            f"{use_speedups}"
        )

        print(
            f"[MONSTER] Canavar önceliği: "
            f"{preferred_monsters}"
        )