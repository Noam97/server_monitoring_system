from fastapi import APIRouter, HTTPException
from app.schemas import ServerCreate, ServerOut, ServerUpdate, ServerDetailOut
from app.repositories.server_repository import (
    add_server as add_server_to_db, 
    get_all_servers,
    get_server_by_id,
    update_server,
    delete_server,
)


router = APIRouter()

@router.get("/", response_model=list[ServerOut])
def get_servers():
    return get_all_servers()

@router.get("/{server_id}", response_model=ServerDetailOut)
def get_server(server_id: int):
    result = get_server_by_id(server_id)
    if not result:
        raise HTTPException(status_code=404, detail="Server not found")
    
    server, logs = result
    return {
        "id": server.id,
        "name": server.name,
        "url": server.url,
        "protocol": server.protocol,
        "logs": logs
    }

@router.post("/", response_model=ServerOut, status_code=201)
def add_server(server_data: ServerCreate):
    return add_server_to_db(server_data)

@router.patch("/{server_id}", response_model=ServerOut)
def patch_server(server_id: int, server_data: ServerUpdate):
    server = update_server(server_id, server_data)
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")
    return server

@router.delete("/{server_id}", status_code=204)
def remove_server(server_id: int):
    deleted = delete_server(server_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Server not found")
