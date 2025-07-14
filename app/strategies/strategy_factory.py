from app.strategies.http_strategy import HttpMonitorStrategy
# from strategies.ftp_strategy import FtpMonitorStrategy
# from strategies.ssh_strategy import SshMonitorStrategy

class MonitorStrategyFactory:
    @staticmethod
    def get_strategy(protocol: str):
        protocol = protocol.lower()
        
        if protocol in ["http", "https"]:
            return HttpMonitorStrategy()
        
        # elif protocol == "ftp":
        #     return FtpMonitorStrategy()
        # elif protocol == "ssh":
        #     return SshMonitorStrategy()
        
        else:
            raise ValueError(f"Unsupported protocol: {protocol}")
