from morning_greetings.contacts_manager import ContactsManager
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_message
from morning_greetings.logger import log_message

def main():
    contacts_manager = ContactsManager()
    contacts = contacts_manager.get_contacts()

    for contact in contacts:
        name = contact['name']
        email = contact['email']
        message = generate_message(name)

        try:
            send_message(email, message)
            print(f"Sending message to {name}")
            log_message(contact, message)  # This should log the message in message_log.txt
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
