import time
from app.strategies.base_strategy import MonitorStrategy
import paramiko

class SSHMonitorStrategy(MonitorStrategy):
    def check(self, server) -> tuple:
        start_time = time.time()
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(server.url, username=server.username, password=server.password, timeout=45)
            ssh.close()
            duration = time.time() - start_time
            return True, duration, 200
        except Exception as e:
            duration = time.time() - start_time
            print(f"[SSH ERROR] Could not connect to {server.url}: {e}")
            return False, duration, 530

