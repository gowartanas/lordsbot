from core.task import BaseTask


class MirageTask(BaseTask):

    def __init__(self):
        super().__init__(
            name="Serap Diyarı",
            enabled=True,
            priority=3
        )

        self.settings = {}

    def configure(self, settings):

        self.settings = settings or {}

        self.enabled = bool(
            self.settings.get(
                "mirageEnabled",
                False
            )
        )

    def run(self):

        auto_enter = self.settings.get(
            "mirageAutoEnter",
            False
        )

        auto_attack = self.settings.get(
            "mirageAutoAttack",
            False
        )

        attack_level = self.settings.get(
            "mirageAttackLevel",
            1
        )

        use_energy = self.settings.get(
            "mirageUseEnergy",
            False
        )

        use_speedups = self.settings.get(
            "mirageUseSpeedups",
            False
        )

        print(
            "[MIRAGE] Serap Diyarı görevi çalıştı."
        )

        print(
            f"[MIRAGE] Otomatik giriş: {auto_enter}"
        )

        print(
            f"[MIRAGE] Otomatik saldırı: {auto_attack}"
        )

        print(
            f"[MIRAGE] Saldırı seviyesi: {attack_level}"
        )

        print(
            f"[MIRAGE] Enerji kullan: {use_energy}"
        )

        print(
            f"[MIRAGE] Hızlandırma kullan: {use_speedups}"
        )