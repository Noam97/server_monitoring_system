import asyncio
from app.models import SessionLocal
from app.models.server import Server
from app.services.ping_service import ping_server

async def start_pinging_loop():
    while True:
        session = SessionLocal()
        servers = session.query(Server).all()
        session.close()

        tasks = [ping_server(server) for server in servers]
        await asyncio.gather(*tasks)

        await asyncio.sleep(30)  # פינג כל 30 שניות
