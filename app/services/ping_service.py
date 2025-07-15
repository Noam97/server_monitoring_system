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
        result = monitor.run_check()
        success = result["success"]
        duration = result["response_time"]
        code = result["code"]

        log = RequestLog(
            server_id=server.id,
            success=success,
            response_time=duration if duration is not None else 0.0,
            status_code=code
        )

        session.add(log)
        session.commit()

    except Exception as e:
        print(f"[ERROR] Failed to ping {server.url}: {e}")
        session.rollback()

    finally:
        session.close()