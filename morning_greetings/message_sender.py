import re

def send_message(email, message):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        raise ValueError("Invalid email address")
    if not message:
        raise ValueError("Message cannot be empty")
    print(f"Sending message to {email}: {message}")