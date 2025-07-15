# from db.base import Base, SessionLocal
# from .server import Server
# from .request_log import RequestLog
# from app.models.ftp_server import FTPServer
# from app.models.http_server import HTTPServer
# from app.models.https_server import HTTPSServer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .server import Server
from .request_log import RequestLog
