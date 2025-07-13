from datetime import datetime

class RequestLog:
    def __init__(self, server_id: int, success: bool, response_time: float, status_code: str, timestamp=None):
        self.server_id = server_id
        self.success = success
        self.response_time = response_time
        self.status_code = status_code
        self.timestamp = timestamp or datetime.utcnow()

    def __repr__(self):
        return (
            f"<RequestLog server_id={self.server_id} "
            f"success={self.success} response_time={self.response_time} "
            f"status_code={self.status_code} timestamp={self.timestamp}>"
        )
