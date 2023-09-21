import smtplib
import imghdr
from email.message import EmailMessage

SENDER = "disha01423@gmail.com"
PASSWORD = "sevarvvtsncordbj"
RECEIVER = "disha25ai016@satiengg.in"


def send_emails(image_path):
    print("send_emails function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey!, we just found a new customer!!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send_emails function ended")


if __name__ == "__main__":
    send_emails(image_path=r"images/40.png")
