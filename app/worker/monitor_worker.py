from models.server import Server
from models.request_log import RequestLog
from services.server_monitor import ServerMonitor
from services.email_service import send_email_alert

# TODO: Save this log entry to the database instead of in-memory list
request_logs = []
def monitor_all_servers(servers):
    for server in servers:
        print(f"Checking server: {server.name} ({server.url})")

        monitor = ServerMonitor(server)
        success, duration, code = monitor.run_check()

        log = RequestLog(server.id, success, duration, code)
        request_logs.append(log)
        print(f" -> Result: success={success}, time={duration:.2f}s, code={code}")

        recent_logs = [r for r in reversed(request_logs) if r.server_id == server.id]
        recent_failures = [r for r in recent_logs if not r.success][:3]

        if len(recent_failures) == 3:
            print(f"Server {server.name} failed 3 times! Would send email here.")
            send_email_alert(server)
