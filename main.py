from fastapi import FastAPI
from app.routes.server_routes import router as server_router
from app.services.background_pinger import start_pinging_loop 
import asyncio 

app = FastAPI()

@app.on_event("startup")
async def start_background_tasks():
    asyncio.create_task(start_pinging_loop())

app.include_router(server_router, prefix="/servers", tags=["Servers"])
