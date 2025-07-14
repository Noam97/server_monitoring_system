from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, HttpUrl
from app.models.server import Protocol

class ServerCreate(BaseModel):
    name: str
    url: str
    protocol: Protocol
    is_healthy: Optional[bool] = None


class ServerOut(BaseModel):
    id: int
    name: str
    url: str
    protocol: Protocol
    is_healthy: Optional[bool] = None

    class Config:
        from_attributes = True

class RequestLogOut(BaseModel):
    success: bool
    response_time: float
    status_code: str
    timestamp: datetime

    class Config:
        from_attributes = True

class ServerDetailOut(ServerOut):
    logs: List[RequestLogOut]

class ServerUpdate(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None
    protocol: Optional[Protocol] = None
    is_healthy: Optional[bool] = None

