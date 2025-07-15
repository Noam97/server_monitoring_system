from email.mime.text import MIMEText
import smtplib
from app import config

def send_server_down_email(server):
    subject = f"[ALERT] Server '{server.name}' is DOWN"
    message = (
        f"⚠️ Server Failure Detected ⚠️\n\n"
        f"The server at {server.url} using protocol '{server.protocol}'\n"
        f"has failed 3 consecutive health checks.\n\n"
        f"Please investigate the issue as soon as possible.\n"
    )

    print("=" * 60)
    print("📧 Sending Email Alert")
    print(f"Subject: {subject}")
    print(f"Body:\n{message}")
    print("=" * 60)

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = config.SMTP_USER
    msg['To'] = config.ALERT_EMAIL

    print("SMTP_USER:", config.SMTP_USER)
    print("SMTP_PASSWORD:", config.SMTP_PASSWORD)
    print("ALERT_EMAIL:", config.ALERT_EMAIL)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(config.SMTP_USER, config.SMTP_PASSWORD)
            smtp.send_message(msg)
        print("✅ Email alert sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email alert: {e}")
