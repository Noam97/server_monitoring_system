import httpx
import time
from app.models import SessionLocal
from app.models.server import Server
from app.models.request_log import RequestLog

async def ping_server(server: Server):
    url = f"{server.protocol}://{server.url}"
    session = SessionLocal()

    try:
        start_time = time.monotonic()
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=10)
        elapsed = time.monotonic() - start_time

        log = RequestLog(
            server_id=server.id,
            success=True,
            response_time=elapsed,
            status_code=str(response.status_code)
        )
    except Exception:
        elapsed = time.monotonic() - start_time
        log = RequestLog(
            server_id=server.id,
            success=False,
            response_time=elapsed,
            status_code="ERR"
        )
    finally:
        session.add(log)
        session.commit()
        session.close()
