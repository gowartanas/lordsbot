import logging
import os

from .state import BotStatus
from .task_manager import TaskManager
from modules.registry import ModuleRegistry


class BotEngine:

    def __init__(self):

        self.status = BotStatus.IDLE
        self.task_delay = 5
        self.settings = {}

        self.registry = ModuleRegistry()
        self.task_manager = TaskManager(self)

        log_dir = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "logs"
            )
        )

        os.makedirs(log_dir, exist_ok=True)

        logging.basicConfig(
            filename=os.path.join(
                log_dir,
                "bot.log"
            ),
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s"
        )

    def configure(self, settings):

        settings = settings or {}
        self.settings = dict(settings)

        try:
            self.task_delay = int(
                settings.get("taskDelay", 5) or 5
            )
        except (ValueError, TypeError):
            self.task_delay = 5

        module_settings = {
            "Kaynak Toplama": "gatherEnabled",
            "Koruma": "shieldEnabled",
            "Krallık Desteği": "supportEnabled",
            "Serap Diyarı": "mirageEnabled",
            "Canavar Avı": "monsterEnabled",
            "Rally": "rallyEnabled",
            "Cargo": "cargoEnabled",
            "Bina Geliştirme": "buildingEnabled",
            "Araştırma": "researchEnabled",
            "Ordu": "armyEnabled",
            "Kahramanlar": "heroesEnabled",
            "Ekipman": "equipmentEnabled",
            "Familiars": "familiarsEnabled",
            "Banka": "bankEnabled"
        }

        for task in self.registry.get_all():

            setting_key = module_settings.get(task.name)

            if setting_key:
                task.enabled = bool(
                    settings.get(
                        setting_key,
                        False
                    )
                )

            if hasattr(task, "configure"):
                task.configure(settings)

        logging.info("Bot ayarları güncellendi.")

        logging.info(
            "Task delay: %s",
            self.task_delay
        )

        logging.info(
            "Aktif modüller: %s",
            [task.name for task in self.registry.enabled()]
        )

    def start(self):

        if self.status == BotStatus.RUNNING:
            return False

        self.status = BotStatus.STARTING

        logging.info("Bot başlatılıyor.")

        self.tasks = self.registry.enabled()

        print()
        print("=" * 50)
        print("[ENGINE] AKTİF GÖREVLER:")

        for task in self.tasks:
            print("[ENGINE] ->", task.name)

        print("=" * 50)
        print()

        logging.info(
            "Aktif görevler: %s",
            [task.name for task in self.tasks]
        )

        self.task_manager.set_tasks(self.tasks)
        self.task_manager.start()

        self.status = BotStatus.RUNNING

        logging.info("Bot çalışıyor.")

        return True

    def stop(self):

        if self.status == BotStatus.IDLE:
            return False

        self.status = BotStatus.STOPPING

        self.task_manager.stop()

        self.status = BotStatus.IDLE

        logging.info("Bot durduruldu.")

        return True

    def handle_error(self, task, exc):

        logging.exception(
            "Görev hatası: %s | %s",
            getattr(task, "name", "unknown"),
            exc
        )

        print(
            "[ENGINE] GÖREV HATASI:",
            getattr(task, "name", "unknown"),
            "|",
            exc
        )