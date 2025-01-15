import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config


def send_registration_email(to_email, account_no, sender_email):
    """Sends a registration confirmation email."""
    email_host = Config.EMAIL_HOST
    email_port = Config.EMAIL_PORT
    email_user = Config.EMAIL_USER
    email_password = Config.EMAIL_PASSWORD

    subject = "Welcome to Trade Beacon Smart Trading!"
    body = f"Dear User,\n\nYour account has been successfully registered with account number: {account_no}. \n\n\nBest regards,\nThe Trade Beacon Team"

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(email_host, email_port) as server:
            server.starttls()
            server.login(email_user, email_password)
            server.send_message(message)
        print("Email sent successfully!")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False