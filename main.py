import schedule
import time
from morning_greetings.contacts_manager import ContactsManager
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_message
from morning_greetings.logger import log_message

def send_morning_greetings():
    """
    Send personalized greetings to all contacts in the contact list.
    """
    contacts_manager = ContactsManager()
    contacts = contacts_manager.get_contacts()

    for contact in contacts:
        name = contact['name']
        email = contact['email']
        message = generate_message(name)

        try:
            print(f"Sending message to {name}")  # Debug statement to verify message sending
            send_message(email, message)
            log_message(contact, message)  # Log the message after it is sent
        except ValueError as e:
            print(f"Error: {e}")



# Schedule the greetings to be sent every day at 8:00 AM
schedule.every().day.at("08:00").do(send_morning_greetings)

# Keep the script running and checking the schedule
while True:
    schedule.run_pending()
    time.sleep(60)


"""
# Schedule the greetings to be sent every 10 seconds for test case
schedule.every(10).seconds.do(send_morning_greetings)


# Keep the script running and checking the schedule every 5 second for test case
while True:
    schedule.run_pending()
    time.sleep(5)
"""