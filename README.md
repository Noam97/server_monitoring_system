# Server Monitoring System

A cloud-based system for monitoring servers using multiple protocols (HTTP, HTTPS, and soon FTP/SSH).  
The system performs periodic health checks, maintains historical logs, and raises email alerts when a server becomes unhealthy.

---

## Features

- Add / edit / delete / list servers
- Health check every 1 minute (async background loop)
- Logs all monitoring requests in history table
- Mark server as Healthy after 5 successful responses
- Mark server as Unhealthy after 3 failed responses
- View server health status and full request history
- Query health status of a server at a given timestamp
- RESTful API with clear endpoints
- Email alert when a server becomes unhealthy
- Built with Python, FastAPI, SQLAlchemy, MySQL

---

## Getting Started

### 1. Clone the repository

git clone https://github.com/Noam97/server_monitoring_system.git
cd server_monitoring_system


### 2. Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt


### 4. Set up the database

## Make sure you have a MySQL server running.

Create a new database and configure the connection URL inside app/config.py:
  DB_URL = "mysql+pymysql://<user>:<password>@localhost/<your_db_name>"
  
## Then run:
python db/init_db.py


### 5. Run the application
uvicorn main:app --reload

### API Endpoints
You can use the included Postman collection to test the following:

POST /servers – Create server

GET /servers – Get all servers

GET /servers/{id} – Get server + last 10 logs

PATCH /servers/{id} – Update server

DELETE /servers/{id} – Delete server

GET /servers/with-health – Get all servers with health status

GET /servers/requests/{id} – Get all request logs for specific server

GET /servers/was-healthy/{id}?timestamp=... – Was server healthy at given timestamp


###  Postman Collection


### SQL DB Dump


### Tech Stack
- Python 3.10+
- FastAPI
- SQLAlchemy
- MySQL
- Uvicorn
- Requests / httpx








