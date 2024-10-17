import datetime
import os

LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), '../message_log.txt')

def log_message(contact, message):
    with open(LOG_FILE_PATH, "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - Sent to {contact['name']} ({contact['email']}): {message}\n")
