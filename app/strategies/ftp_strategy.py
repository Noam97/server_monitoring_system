from ftplib import FTP
import time
from app.strategies.base_strategy import MonitorStrategy


class FTPMonitorStrategy(MonitorStrategy):
    def check(self, server) -> dict:
        start_time = time.time()
        success = None
        code = None
        try:
            ftp = FTP()
            ftp.connect(host=server.url, timeout=45)
            ftp.login(user="demo", passwd="password")
            ftp.quit()

            response_time = time.time() - start_time
            return {
                "success": response_time < 45,
                "response_time": response_time,
                "code": 230
            }
        except Exception as e:
            print(f"[FTP ERROR] Could not connect to {server.url}: {e}")
            return {
                "success": False,
                "response_time":0.0,
                "code": 530
            }
