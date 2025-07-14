from fastapi import APIRouter, HTTPException
from datetime import datetime
from app.repositories.server_repository import (
    get_all_servers,
    get_server_by_id,
    get_server_with_logs,
    add_server,
    update_server,
    delete_server
)
from app.schemas import ServerCreate, ServerUpdate

router = APIRouter()

@router.get("/")
def get_servers():
    return get_all_servers()

@router.get("/health-status")
def get_all_servers_with_health():
    servers = get_all_servers()
    return [
        {
            "id": server.id,
            "name": server.name,
            "url": server.url,
            "protocol": server.protocol,
            "is_healthy": server.is_healthy
        }
        for server in servers
    ]

@router.get("/{server_id}")
def get_server(server_id: int, include_logs: bool = True):
    if include_logs:
        result = get_server_with_logs(server_id)
        if not result or result[0] is None:
            raise HTTPException(status_code=404, detail="Server not found")
        server, logs = result
        return {"server": server, "logs": logs}
    else:
        server = get_server_by_id(server_id)
        if not server:
            raise HTTPException(status_code=404, detail="Server not found")
        return server

@router.post("/")
def create_server(server_data: ServerCreate):
    return add_server(server_data)

@router.patch("/{server_id}")
def edit_server(server_id: int, server_data: ServerUpdate):
    updated = update_server(server_id, server_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Server not found")
    return updated

@router.delete("/{server_id}")
def remove_server(server_id: int):
    result = delete_server(server_id)
    if not result:
        raise HTTPException(status_code=404, detail="Server not found")
    return {"message": "Server deleted"}



@router.get("/health-status/{server_id}")
def get_server_health(server_id: int):
    server = get_server_by_id(server_id)

    if not server:
        raise HTTPException(status_code=404, detail="Server not found")
    
    return {"is_healthy": server.is_healthy}

@router.get("/was-healthy/{server_id}")
def was_healthy_at(server_id: int, timestamp: datetime):
    from app.repositories import server_repository

    logs = server_repository.get_logs_before_timestamp(server_id, timestamp, limit=5)

    if len(logs) < 5:
        return {"was_healthy": False}

    was_healthy = all(log.success for log in logs)
    return {"was_healthy": was_healthy}


@router.get("/logs/{server_id}")
def get_server_request_logs(server_id: int):
    from app.repositories import server_repository
    
    logs = server_repository.get_request_logs_by_server_id(server_id)
    
    if not logs:
        raise HTTPException(status_code=404, detail="No logs found for this server")

    return [
        {
            "timestamp": log.timestamp,
            "success": log.success,
            "response_time": log.response_time,
            "status_code": log.status_code
        }
        for log in logs
    ]