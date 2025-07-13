from abc import ABC, abstractmethod

class MonitorStrategy(ABC):
    MAX_ALLOWED_TIME = 45.0
    @abstractmethod
    def check(self, server):
        """
        Run a health check on the given server.
        This method must be implemented by any strategy.
        """
        pass