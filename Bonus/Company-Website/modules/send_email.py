import smtplib
import ssl
import os


def send_email(message) -> None:
    """
    Send a Email from the same Source and Destination address
    """
    host = "smtp.gmail.com"
    port = 465
    # Get values from OS Environment Variables (more secure)
    username = os.getenv("EMAIL_PYTHON")
    password = os.getenv("EMAIL_PYTHON_PW")
    receiver = os.getenv("EMAIL_PYTHON")
    # Create a secure context with Secure Sockets Layer (SSL) certificate
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
