from abc import ABC, abstractmethod


class BaseTask(ABC):

    def __init__(self, name, enabled=True, priority=0):
        self.name = name
        self.enabled = enabled
        self.priority = priority

    def is_ready(self):
        return self.enabled

    @abstractmethod
    def run(self):
        pass

    def stop(self):
        pass