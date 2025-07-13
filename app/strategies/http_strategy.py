import requests
import time
from strategies.base_strategy import MonitorStrategy

# A strategy class to monitor servers using HTTP protocol
class HttpMonitorStrategy(MonitorStrategy):
    def check(self, server):
        MAX_ALLOWED_TIME = 45.0
        try:
            start = time.time()
            response = requests.get(server.url, timeout=45)
            duration = time.time() - start
            # Consider it a success if the response status code is 2xx and time < 45 seconds
            success = 200 <= response.status_code < 300 and duration < 45
            return success, duration, str(response.status_code)
        except Exception as e:
            return False, self.MAX_ALLOWED_TIME + 1, str(e)




