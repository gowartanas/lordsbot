from core.task import BaseTask


class CargoTask(BaseTask):

    def __init__(self):
        super().__init__(
            name="Cargo",
            enabled=True,
            priority=6
        )

        self.settings = {}

    def configure(self, settings):

        self.settings = settings or {}

        self.enabled = bool(
            self.settings.get(
                "cargoEnabled",
                False
            )
        )

    def run(self):

        auto_send = self.settings.get(
            "cargoAutoSend",
            False
        )

        cargo_type = self.settings.get(
            "cargoType",
            "resource"
        )

        resource_priority = self.settings.get(
            "cargoResourcePriority",
            ["food", "wood", "stone", "ore", "gold"]
        )

        max_amount = self.settings.get(
            "cargoMaxAmount",
            0
        )

        protect_cargo = self.settings.get(
            "cargoProtect",
            True
        )

        print("[CARGO] Cargo görevi çalıştı.")
        print(f"[CARGO] Otomatik gönder: {auto_send}")
        print(f"[CARGO] Cargo tipi: {cargo_type}")
        print(f"[CARGO] Kaynak önceliği: {resource_priority}")
        print(f"[CARGO] Maksimum miktar: {max_amount}")
        print(f"[CARGO] Cargo koruması: {protect_cargo}")