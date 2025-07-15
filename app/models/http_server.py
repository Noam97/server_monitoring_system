from sqlalchemy import Column, Integer, ForeignKey
from app.models.server import Server

class HTTPServer(Server):
    # __tablename__ = "http_servers"

    # id = Column(Integer, ForeignKey("servers.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "http"
    }
