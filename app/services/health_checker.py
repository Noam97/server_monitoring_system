from datetime import datetime
from app.repositories.request_repository import RequestRepository
from app.repositories.server_repository import get_server_with_logs, update_server
from app.services.email_service import send_server_down_email
from app.schemas import ServerUpdate 

HEALTHY_THRESHOLD = 5
UNHEALTHY_THRESHOLD = 3
def evaluate_server_health(server_id):
    recent_logs = RequestRepository.get_recent_logs(server_id, limit=HEALTHY_THRESHOLD)
    if len(recent_logs) < UNHEALTHY_THRESHOLD:
        return

    server, _ = get_server_with_logs(server_id)
    if not server:
        return

    now = datetime.utcnow()

    if len(recent_logs) >= HEALTHY_THRESHOLD and all(log.success for log in recent_logs[:HEALTHY_THRESHOLD]):
        if server.is_healthy is not True:
            update_server(server.id, ServerUpdate(is_healthy=True, last_health_status_sent=now))
        return

    if all(not log.success for log in recent_logs[:UNHEALTHY_THRESHOLD]):
        if server.is_healthy is not False:
            update_server(server.id, ServerUpdate(is_healthy=False, last_health_status_sent=now))
            send_server_down_email(server)
        return