import smtplib
import os
from email.message import EmailMessage


def send_email(message) -> None:
    """
    Send a Email from the same Source and Destination address
    """
    # Create the email content
    email_message = EmailMessage()
    email_message["Subject"] = "New Event was Found!"
    email_message.set_content(message)
    # Get values from OS Environment Variables (more secure)
    username = os.getenv("EMAIL_PYTHON")
    password = os.getenv("EMAIL_PYTHON_PW")
    receiver = os.getenv("EMAIL_PYTHON")

    gmail = smtplib.SMTP(host="smtp.gmail.com", port=587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username, password)
    gmail.sendmail(username, receiver, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email()