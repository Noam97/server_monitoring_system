from strategies.strategy_factory import MonitorStrategyFactory
from models.server import Server

class ServerMonitor:
    def __init__(self, server: Server):
        self.server = server
        # Use the factory to get the appropriate strategy for the server's protocol
        self.strategy = MonitorStrategyFactory.get_strategy(server.protocol)

    def run_check(self):
        # Run the check using the selected strategy
        result = self.strategy.check(self.server)
        return result
