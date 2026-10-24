from modules.gathering import GatheringTask
from modules.protection import ProtectionTask
from modules.support import SupportTask
from modules.mirage import MirageTask
from modules.monster import MonsterTask
from modules.rally import RallyTask
from modules.cargo import CargoTask
from modules.building import BuildingTask
from modules.research import ResearchTask
from modules.army import ArmyTask
from modules.heroes import HeroesTask
from modules.equipment import EquipmentTask
from modules.familiars import FamiliarsTask
from modules.bank import BankTask


class ModuleRegistry:

    def __init__(self):

        self.modules = {}

        self.register(GatheringTask())
        self.register(ProtectionTask())
        self.register(SupportTask())
        self.register(MirageTask())
        self.register(MonsterTask())
        self.register(RallyTask())
        self.register(CargoTask())
        self.register(BuildingTask())
        self.register(ResearchTask())
        self.register(ArmyTask())
        self.register(HeroesTask())
        self.register(EquipmentTask())
        self.register(FamiliarsTask())
        self.register(BankTask())

    def register(self, module):
        self.modules[module.name] = module

    def get(self, name):
        return self.modules.get(name)

    def get_all(self):
        return list(self.modules.values())

    def enabled(self):
        return [
            module
            for module in self.modules.values()
            if module.enabled
        ]

    def disable_all(self):
        for module in self.modules.values():
            module.enabled = False

    def enable(self, name):
        module = self.get(name)

        if module:
            module.enabled = True

    def disable(self, name):
        module = self.get(name)

        if module:
            module.enabled = False