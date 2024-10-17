import datetime
import os

LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), '../message_log.txt')

def log_message(contact, message):
    """
    Log the details of a sent message.
    
    Args:
        contact (dict): A dictionary containing contact information, such as 'name' and 'email'.
        message (str): The message that was sent.
    
    Logs the timestamp, contact name, email, and the message to 'message_log.txt'.
    """
    with open(LOG_FILE_PATH, "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - Sent to {contact['name']} ({contact['email']}): {message}\n")
