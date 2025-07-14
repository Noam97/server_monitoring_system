def send_email_alert(server):
  # TODO: Replace with actual email sending logic using SMTP or an email service
  #Sends an email alert when a server fails 3 times in a row
    print("Sending email alert!")
    print(f"Subject: Server '{server.name}' is DOWN")
    print(f"Message: The server at {server.url} has failed 3 consecutive checks.\n"
          f"Please investigate the issue.")


def send_server_down_email(server):
    """
    Simulates sending an email alert when a server becomes unhealthy.
    This function prints the email contents to the console.
    In a real-world scenario, this should be replaced with actual SMTP logic.

    :param server: Server object containing server name and URL
    """
    subject = f"[ALERT] Server '{server.name}' is DOWN"
    message = (
        f"⚠️ Server Failure Detected ⚠️\n\n"
        f"The server at {server.url} using protocol '{server.protocol}'\n"
        f"has failed 3 consecutive health checks.\n\n"
        f"Please investigate the issue as soon as possible.\n"
    )

    print("=" * 60)
    print("Sending Email Alert (Simulation Only)")
    print(f"Subject: {subject}")
    print(f"Body:\n{message}")
    print("=" * 60)
