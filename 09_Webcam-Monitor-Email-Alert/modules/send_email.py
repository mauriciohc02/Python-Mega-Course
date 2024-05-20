import smtplib
import os
from email.message import EmailMessage
import imghdr


def send_email(image_path):
    """
    Send a Email with attached image from the same Source and Destination address
    """
    # Create the email content
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")
    # Read the image
    with open(image_path, "rb") as file:
        image = file.read()
    # Attach the image to the email
    email_message.add_attachment(image, maintype="image", subtype=imghdr.what(None, image))
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
    send_email(image_path="./images/19.png")