def send_email_alert(server):
  # TODO: Replace with actual email sending logic using SMTP or an email service
  #Sends an email alert when a server fails 3 times in a row
    print("Sending email alert!")
    print(f"Subject: Server '{server.name}' is DOWN")
    print(f"Message: The server at {server.url} has failed 3 consecutive checks.\n"
          f"Please investigate the issue.")
