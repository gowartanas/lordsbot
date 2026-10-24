from core.task import BaseTask


class HeroesTask(BaseTask):

    def __init__(self):
        super().__init__(
            name="Kahramanlar",
            enabled=True,
            priority=10
        )

        self.settings = {}

    def configure(self, settings):
        self.settings = settings or {}

        self.enabled = bool(
            self.settings.get(
                "heroesEnabled",
                False
            )
        )

    def run(self):

        auto_upgrade = self.settings.get(
            "heroesAutoUpgrade",
            False
        )

        auto_assign = self.settings.get(
            "heroesAutoAssign",
            False
        )

        priority = self.settings.get(
            "heroesPriority",
            []
        )

        use_resources = self.settings.get(
            "heroesUseResources",
            False
        )

        print("[HEROES] Kahraman görevi çalıştı.")
        print(f"[HEROES] Otomatik geliştirme: {auto_upgrade}")
        print(f"[HEROES] Otomatik atama: {auto_assign}")
        print(f"[HEROES] Kahraman önceliği: {priority}")
        print(f"[HEROES] Kaynak kullan: {use_resources}")