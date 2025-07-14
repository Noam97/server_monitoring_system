from app.models import SessionLocal
from app.models.server import Server
from app.services.ping_service import ping_server
from app.services.health_checker import evaluate_server_health
import asyncio


async def start_pinging_loop():
    while True:
        session = SessionLocal()
        servers = session.query(Server).all()
        session.close()

        async def ping_and_evaluate(server):
            await ping_server(server)
            evaluate_server_health(server.id)

        tasks = [ping_and_evaluate(server) for server in servers]
        await asyncio.gather(*tasks)

        await asyncio.sleep(30)
