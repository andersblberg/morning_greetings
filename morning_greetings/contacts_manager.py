# contacts_manager.py

class ContactsManager:
    def __init__(self):
        self.contacts = [
            {"name": "Bjarne", "email": "Bjarne@google.com", "preferred_time": "08:00 AM"},
            {"name": "Kurt", "email": "Kurt@google.com", "preferred_time": "08:00 AM"},
            {"name": "Rune", "email": "Rune@google.com", "preferred_time": "08:00 AM"}
        ]

    def add_contact(self, name, email, preferred_time="08:00 AM"):
        contact = {
            'name': name,
            'email': email,
            'preferred_time': preferred_time
        }
        self.contacts.append(contact)

    def remove_contact(self, name):
        self.contacts = [c for c in self.contacts if c['name'] != name]

    def get_contacts(self):
        return self.contacts

    def list_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}")
