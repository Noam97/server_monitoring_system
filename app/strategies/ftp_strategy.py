from ftplib import FTP
import time
from app.strategies.base_strategy import MonitorStrategy

class FTPMonitorStrategy(MonitorStrategy):
    def check(self, server) -> tuple:
        start_time = time.time()
        try:
            ftp = FTP()
            ftp.connect(host=server.url, timeout=45)
            ftp.login(user="demo", passwd="password")
            ftp.quit()
            duration = time.time() - start_time
            return True, duration, 200
        except Exception as e:
            duration = time.time() - start_time
            print(f"[FTP ERROR] Could not connect to {server.url}: {e}")
            return False, duration, 530
