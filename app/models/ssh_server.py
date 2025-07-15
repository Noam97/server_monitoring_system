from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.server import Server

class SSHServer(Server):
    __tablename__ = "ssh_servers"
    id = Column(Integer, ForeignKey("servers.id"), primary_key=True)
    username = Column(String(100), nullable=True)
    password = Column(String(100), nullable=True)
    private_key_path = Column(String(500), nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "ssh"
    }
