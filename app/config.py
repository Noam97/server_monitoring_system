import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

DB_URL = os.getenv("DB_URL")

SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
ALERT_EMAIL = os.getenv("ALERT_EMAIL")