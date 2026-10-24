from core.task import BaseTask


class SupportTask(BaseTask):

    def __init__(self):
        super().__init__(
            name="Krallık Desteği",
            enabled=True,
            priority=2
        )

        self.settings = {}

    def configure(self, settings):
        self.settings = settings or {}

        self.enabled = bool(
            self.settings.get(
                "supportEnabled",
                False
            )
        )

    def run(self):
        send_food = self.settings.get(
            "supportFood",
            False
        )

        send_wood = self.settings.get(
            "supportWood",
            False
        )

        send_stone = self.settings.get(
            "supportStone",
            False
        )

        send_ore = self.settings.get(
            "supportOre",
            False
        )

        send_gold = self.settings.get(
            "supportGold",
            False
        )

        amount = self.settings.get(
            "supportAmount",
            0
        )

        priority = self.settings.get(
            "supportPriority",
            []
        )

        print(
            "[SUPPORT] Krallık desteği görevi çalıştı."
        )

        print(
            f"[SUPPORT] Miktar: {amount}"
        )

        print(
            f"[SUPPORT] Yemek: {send_food} | "
            f"Odun: {send_wood}"
        )

        print(
            f"[SUPPORT] Taş: {send_stone} | "
            f"Cevher: {send_ore}"
        )

        print(
            f"[SUPPORT] Altın: {send_gold}"
        )

        print(
            f"[SUPPORT] Öncelik: {priority}"
        )