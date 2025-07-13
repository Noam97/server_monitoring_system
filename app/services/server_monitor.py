from strategies.strategy_factory import MonitorStrategyFactory
from models.server import Server

class ServerMonitor:
    def __init__(self, server: Server):
        self.server = server
        self.strategy = MonitorStrategyFactory.get_strategy(server.protocol)

    def run_check(self):
        result = self.strategy.check(self.server)
        return result
