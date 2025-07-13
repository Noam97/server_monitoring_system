from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from app.config import DB_URL

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
