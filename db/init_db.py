from sqlalchemy import create_engine
from app.models import Base
from app import config
from app.models import server, request_log

engine = create_engine(config.DB_URL)

Base.metadata.create_all(engine)

print("Database and tables created successfully.")
