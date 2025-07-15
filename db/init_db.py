from sqlalchemy import create_engine
from app.config import DB_URL
from db.base import Base

from app.models import server, request_log, http_server, https_server, ftp_server

engine = create_engine(DB_URL)
Base.metadata.create_all(engine)

print("All tables created successfully.")