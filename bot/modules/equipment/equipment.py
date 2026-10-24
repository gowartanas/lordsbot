from core.task import BaseTask


class EquipmentTask(BaseTask):

    def __init__(self):
        super().__init__(
            name="Ekipman",
            enabled=True,
            priority=11
        )

        self.settings = {}

    def configure(self, settings):
        self.settings = settings or {}

        self.enabled = bool(
            self.settings.get(
                "equipmentEnabled",
                False
            )
        )

    def run(self):

        auto_craft = self.settings.get(
            "equipmentAutoCraft",
            False
        )

        auto_upgrade = self.settings.get(
            "equipmentAutoUpgrade",
            False
        )

        priority = self.settings.get(
            "equipmentPriority",
            []
        )

        use_materials = self.settings.get(
            "equipmentUseMaterials",
            False
        )

        print("[EQUIPMENT] Ekipman görevi çalıştı.")
        print(f"[EQUIPMENT] Otomatik üretim: {auto_craft}")
        print(f"[EQUIPMENT] Otomatik geliştirme: {auto_upgrade}")
        print(f"[EQUIPMENT] Ekipman önceliği: {priority}")
        print(f"[EQUIPMENT] Malzeme kullan: {use_materials}")