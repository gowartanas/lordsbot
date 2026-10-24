from core.task import BaseTask


class BankTask(BaseTask):

    def __init__(self):
        super().__init__(
            name="Banka",
            enabled=True,
            priority=13
        )

        self.settings = {}

    def configure(self, settings):
        self.settings = settings or {}

        self.enabled = bool(
            self.settings.get(
                "bankEnabled",
                False
            )
        )

    def run(self):

        auto_deposit = self.settings.get(
            "bankAutoDeposit",
            False
        )

        auto_collect = self.settings.get(
            "bankAutoCollect",
            False
        )

        minimum_balance = self.settings.get(
            "bankMinimumBalance",
            0
        )

        resource_priority = self.settings.get(
            "bankResourcePriority",
            []
        )

        print("[BANK] Banka görevi çalıştı.")
        print(f"[BANK] Otomatik yatırma: {auto_deposit}")
        print(f"[BANK] Otomatik toplama: {auto_collect}")
        print(f"[BANK] Minimum bakiye: {minimum_balance}")
        print(f"[BANK] Kaynak önceliği: {resource_priority}")