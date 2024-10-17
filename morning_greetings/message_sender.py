import re

def send_message(email, message):
    """
    Send a message to the specified email address.

    Args:
        email (str): The email address of the recipient.
        message (str): The message to be sent.

    Raises:
        ValueError: If the email address is invalid or the message is empty.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        raise ValueError("Invalid email address")
    if not message:
        raise ValueError("Message cannot be empty")
    print(f"Sending message to {email}: {message}")