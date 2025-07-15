from app.models.server import Server
from app.models.request_log import RequestLog
from db.base import SessionLocal
from app.schemas import ServerUpdate
from datetime import datetime
from sqlalchemy.orm import Session

def add_server(server_data):
    session: Session = SessionLocal()
    try:
        new_server = Server(
            name=server_data.name,
            url=str(server_data.url),
            protocol=server_data.protocol
        )
        session.add(new_server)
        session.commit()
        session.refresh(new_server)
        return new_server
    finally:
        session.close()

def get_all_servers():
    session: Session = SessionLocal()
    try:
        servers = session.query(Server).all()
        return servers
    finally:
        session.close()

def get_server_by_id(server_id):
    session: Session = SessionLocal()
    try:
        server = session.query(Server).filter(Server.id == server_id).first()
        return server
    finally:
        session.close()

def get_server_with_logs(server_id: int):
    session: Session = SessionLocal()
    try:
        server = session.query(Server).filter(Server.id == server_id).first()
        if not server:
            return None, []

        logs = (
            session.query(RequestLog)
            .filter(RequestLog.server_id == server_id)
            .order_by(RequestLog.timestamp.desc())
            .limit(10)
            .all()
        )
        return server, logs
    finally:
        session.close()

def delete_server(server_id):
    session: Session = SessionLocal()
    try:
        server = session.query(Server).get(server_id)
        if not server:
            return None
        session.delete(server)
        session.commit()
        return True
    finally:
        session.close()

def update_server(server_id: int, updated_data):
    session: Session = SessionLocal()
    try:
        server = session.query(Server).filter(Server.id == server_id).first()
        if not server:
            return None

        for field, value in updated_data.dict(exclude_unset=True).items():
            setattr(server, field, value)

        session.commit()
        session.refresh(server)
        return server
    finally:
        session.close()

def update_server_object(server: Server):
    session: Session = SessionLocal()
    try:
        session.merge(server)
        session.commit()
    finally:
        session.close()

def get_logs_before_timestamp(server_id: int, timestamp: datetime, limit: int = 5):
    session = SessionLocal()
    try:
        logs = (
            session.query(RequestLog)
            .filter(RequestLog.server_id == server_id)
            .filter(RequestLog.timestamp <= timestamp)
            .order_by(RequestLog.timestamp.desc())
            .limit(limit)
            .all()
        )
        return logs
    finally:
        session.close()


def get_request_logs_by_server_id(server_id: int):
    session = SessionLocal()
    try:
        logs = (
            session.query(RequestLog)
            .filter(RequestLog.server_id == server_id)
            .order_by(RequestLog.timestamp.desc())
            .all()
        )
        return logs
    finally:
        session.close()
