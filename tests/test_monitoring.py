import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models.server import Server
from app.services.server_monitor import ServerMonitor

"""
Test script to manually verify the monitoring logic.
Simulates 2 servers (1 healthy, 1 failing), runs monitoring 3 times.
Useful for local validation and console output review.
"""

print("Starting simple monitoring test!")

servers = [
    Server(id=1, name="Good HTTP", url="https://httpbin.org/status/200", protocol="http"),
    Server(id=2, name="Bad HTTP", url="https://httpbin.org/status/500", protocol="http"),
]

for i in range(3):
    print(f"\nRun {i+1} ------------------------------")
    for server in servers:
        print(f"Checking server: {server.name} ({server.url})")
        monitor = ServerMonitor(server)
        success, duration, code = monitor.run_check()
        print(f" -> Result: success={success}, time={duration:.2f}s, code={code}")

print("\n✅ Finished all monitoring runs. Check output above for success/failure detection.")