from datetime import datetime
from app.models import Base
from sqlalchemy import Column, Integer, String, DateTime

class Server(Base):
    __tablename__ = "servers"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    url = Column(String(255), nullable=False)
    protocol = Column(String(10), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Server {self.name} ({self.protocol})>"
    
    def get_protocol(self):
        return self.protocol
    
    def get_url(self):
        return self.url