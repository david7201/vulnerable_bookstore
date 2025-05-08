import requests
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail import EmailMessage
import os

class BrevoEmailBackend(BaseEmailBackend):
    
    def send_messages(self, email_messages):
        api_key = os.getenv("BREVO_API_KEY")
        if not api_key:
            raise ValueError("BREVO_API_KEY is not set in environment variables.")

        url = "https://api.brevo.com/v3/smtp/email"
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "api-key": api_key,
        }

        for message in email_messages:
            payload = {
                "sender": {"name": "Prodemtion", "email": message.from_email},
                "to": [{"email": recipient} for recipient in message.to],
                "subject": message.subject,
                "htmlContent": message.body,
            }

            response = requests.post(url, json=payload, headers=headers, timeout=5)
            if response.status_code != 201:
                print(f"Failed to send email: {response.json()}")

        return len(email_messages)
