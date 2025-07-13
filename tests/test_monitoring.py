import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from models.server import Server
from worker.monitor_worker import monitor_all_servers

print("Starting monitoring test!")

servers = [
    Server(id=1, name="Good HTTP", url="https://httpbin.org/status/200", protocol="http"),
    Server(id=2, name="Bad HTTP", url="https://httpbin.org/status/500", protocol="http"),
]

for i in range(3):
    print(f"\nRun {i+1} ------------------------------")
    monitor_all_servers(servers)
