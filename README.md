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

## 4. create a `.env` file

Before running the project, create a `.env` file in the root directory based on the `.env.example` provided.

This file contains environment-specific variables such as database connection and email alert credentials.

## Required `.env` variables:

DB_URL=your_database_url

SMTP_USER=servermonitortesting@gmail.com
SMTP_PASSWORD=wwsdxiomtogvzwcm
ALERT_EMAIL=servermonitortesting0@gmail.com

> **Note:**  
> The Gmail account and App Password listed above were created **specifically for this assignment** and are safe to use.  
> This App Password was generated via Google’s [App Password system](https://support.google.com/accounts/answer/185833) and only allows sending emails via SMTP — it cannot be used to log in to Gmail or access any sensitive data.

***If you prefer to use your own email credentials, you can enable 2-Step Verification and generate your own App Password, then replace the values above accordingly.***

### 5. Set up the database

## Make sure you have a MySQL server running.

Create a new database and configure the connection URL inside app/config.py:
  DB_URL = "mysql+pymysql://<user>:<password>@localhost/<your_db_name>"
  
## Then run:
python db/init_db.py


### 6. Run the application
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
The Postman collection can be found in the main folder under the name postman_file.json.
You can import it directly into Postman to test all endpoints.


### SQL DB Dump
The file `server_monitoring_dump.sql` includes the full database schema and example data.  
To restore the database:
mysql -u root -p < server_monitoring_dump.sql


### Tech Stack
- Python 3.10+
- FastAPI
- SQLAlchemy
- MySQL
- Uvicorn
- Requests / httpx


<img width="1249" height="632" alt="image" src="https://github.com/user-attachments/assets/8a9b53be-ef88-4cfe-89cb-e7a815701661" />

<img width="1083" height="416" alt="image" src="https://github.com/user-attachments/assets/167e316c-991c-4761-93f8-342953f10b69" />

<img width="661" height="234" alt="image" src="https://github.com/user-attachments/assets/db8a2ef9-22ea-4dbc-a10d-71a6a7897fb6" />

<img width="855" height="339" alt="image" src="https://github.com/user-attachments/assets/72375a20-9004-4582-977c-a5555d5647d8" />














