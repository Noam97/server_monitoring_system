from sqlalchemy import Column, String, Integer, ForeignKey
from app.models.server import Server

class FTPServer(Server):
    __tablename__ = "ftp_servers"

    id = Column(Integer, ForeignKey("servers.id"), primary_key=True)
    username = Column(String(100), nullable=True)
    password = Column(String(100), nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "ftp"
    }
