from sqlalchemy import Column, Integer, ForeignKey
from app.models.server import Server
from db.base import Base


class HTTPSServer(Server):
    __tablename__ = "https_servers"
    id = Column(Integer, ForeignKey("servers.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "https"
    }
