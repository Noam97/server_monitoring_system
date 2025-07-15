import requests
import time
from app.strategies.base_strategy import MonitorStrategy

class HttpMonitorStrategy(MonitorStrategy):
    def check(self, server) -> dict:
        try:
            url = server.url
            if not url.startswith("http://") and not url.startswith("https://"):
                url = f"{server.protocol}://{url}"

            start = time.time()
            response = requests.get(url, timeout=45)
            duration = time.time() - start
            success = 200 <= response.status_code < 300 and duration < 45

            return {
                "success": success,
                "response_time": duration,
                "code": response.status_code
            }

        except Exception as e:
            print(f"[HTTP ERROR] Could not connect to {server.url}: {e}")
            return {
                "success": False,
                "response_time": 46.0,
                "code": 500
            }
