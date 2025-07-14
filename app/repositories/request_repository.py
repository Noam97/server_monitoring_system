from sqlalchemy.orm import Session
from app.models.request_log import RequestLog
from db.base import SessionLocal

class RequestRepository:
    @staticmethod
    def get_recent_logs(server_id: int, limit: int = 5):
        with SessionLocal() as session:
            return (
                session.query(RequestLog)
                .filter_by(server_id=server_id)
                .order_by(RequestLog.timestamp.desc())
                .limit(limit)
                .all()
            )
