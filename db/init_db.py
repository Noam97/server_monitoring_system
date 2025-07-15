from sqlalchemy import create_engine
from app import config
from app.models import Base

import app.models.server
from app.models.http_server import HTTPServer
from app.models.https_server import HTTPSServer
from app.models.ftp_server import FTPServer
from app.models.ssh_server import SSHServer

import app.models.request_log

engine = create_engine(config.DB_URL)
Base.metadata.create_all(engine)

print("Database and tables created successfully.")
