from datetime import datetime
from app.models import Base
from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime, ForeignKey

class RequestLog(Base):
    __tablename__ = "request_logs"
    id = Column(Integer, primary_key=True)
    server_id = Column(Integer, ForeignKey("servers.id"), nullable=False)
    success = Column(Boolean, nullable=False)
    response_time = Column(Float, nullable=False)
    status_code = Column(String(10), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return (
            f"<RequestLog server_id={self.server_id} "
            f"success={self.success} response_time={self.response_time} "
            f"status_code={self.status_code} timestamp={self.timestamp}>"
        )
