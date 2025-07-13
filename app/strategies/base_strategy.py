from abc import ABC, abstractmethod

class MonitorStrategy(ABC):
    @abstractmethod
    def check(self, server):
        """
        Run a health check on the given server.
        This method must be implemented by any strategy.
        """
        pass