import httpx
import time
from app.models import SessionLocal
from app.models.server import Server
from app.models.request_log import RequestLog

from app.services.server_monitor import ServerMonitor 

async def ping_server(server: Server):
    session = SessionLocal()

    try:
        monitor = ServerMonitor(server)
        success, duration, code = monitor.run_check()

        log = RequestLog(
            server_id=server.id,
            success=success,
            response_time=duration,
            status_code=code
        )
    finally:
        session.add(log)
        session.commit()
        session.close()


