import os
import smtplib
from email.message import EmailMessage

def send_email(to_email: str, summary: str) -> None:
    """
    Sends an email using standard SMTP.
    Requires SMTP_SERVER, SMTP_PORT, EMAIL_SENDER, EMAIL_PASSWORD in environment.
    """
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    sender_email = os.getenv("EMAIL_SENDER")
    sender_password = os.getenv("EMAIL_PASSWORD")

    if not sender_email or not sender_password:
        print("Warning: Email credentials not configured. Simulating email send instead.")
        print(f"--- SIMULATED EMAIL to {to_email} ---")
        print(summary)
        print("---------------------------------------")
        return

    msg = EmailMessage()
    msg.set_content(f"Here is the AI generated sales summary:\n\n{summary}")

    msg['Subject'] = 'Sales Insight Summary'
    msg['From'] = sender_email
    msg['To'] = to_email

    try:
        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        raise RuntimeError(f"Failed to send email via SMTP: {str(e)}")
