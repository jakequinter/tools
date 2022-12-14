import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAILS_TO_SEND = 10

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")


def get_email_info():
    recipient_email = input("To: ")
    subject = input("Subject: ")
    body = input("Body: ")
    message_to_send = f"Subject: {subject}\n\n{body}"

    return recipient_email, message_to_send


def send_emails():
    recipient_email, message_to_send = get_email_info()
    count = 0

    smtp = smtplib.SMTP("smtp.gmail.com", HOST)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL, PASSWORD)

    while count < EMAILS_TO_SEND:
        res = smtp.sendmail(EMAIL, recipient_email, message_to_send)

        if not res:
            print(f"Email {count + 1} has been sent.")
        else:
            print("Error: there was a problem sending your email.")

        count += 1

    smtp.quit()


if __name__ == "__main__":
    send_emails()
