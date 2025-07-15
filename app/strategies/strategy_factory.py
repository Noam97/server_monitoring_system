from app.strategies.http_strategy import HttpMonitorStrategy
from app.strategies.ftp_strategy import FTPMonitorStrategy
from app.strategies.ssh_strategy import SSHMonitorStrategy

class MonitorStrategyFactory:
    @staticmethod
    def get_strategy(protocol: str):
        protocol = protocol.lower()
        
        if protocol in ["http", "https"]:
            return HttpMonitorStrategy()
        
        elif protocol == "ftp":
            return FTPMonitorStrategy()
        elif protocol == "ssh":
            return SSHMonitorStrategy()
        else:
            raise ValueError(f"Unsupported protocol: {protocol}")
