from abc import ABC, abstractmethod

class MonitorStrategy(ABC):
    @abstractmethod
    def check(self, server):
        pass