import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAILS_TO_SEND = 10

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")


def get_email_info():
    recipient_email = input("Enter the email address you wish to send this email: ")
    subject = input("Enter a subject: ")
    body = input("Enter the message body: ")
    message_to_send = f"Subject: {subject}\n{body}"

    return recipient_email, message_to_send


def send_emails():
    recipient_email, message_to_send = get_email_info()
    count = 0

    while count < EMAILS_TO_SEND:
        smtp = smtplib.SMTP("smtp.gmail.com", HOST)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(EMAIL, PASSWORD)
        res = smtp.sendmail(EMAIL, recipient_email, message_to_send)

        if not res:
            print(f"Email {count + 1} has been sent.")
        else:
            print("Error: there was a problem sending your email.")

        count += 1

    smtp.quit()


if __name__ == "__main__":
    send_emails()
