# contacts_manager.py

class ContactsManager:
    """
    A class to manage contacts for the morning greetings application.
    
    Methods:
        add_contact(name, email, time): Adds a new contact to the contact list.
        remove_contact(name): Removes a contact by name from the contact list.
        get_contacts(): Retrieves the current list of contacts.
    """
    def __init__(self):
        self.contacts = [
            {"name": "Bjarne", "email": "Bjarne@google.com", "preferred_time": "08:00 AM"},
            {"name": "Kurt", "email": "Kurt@google.com", "preferred_time": "08:00 AM"},
            {"name": "Rune", "email": "Rune@google.com", "preferred_time": "08:00 AM"}
        ]

    def add_contact(self, name, email, preferred_time="08:00 AM"):
        """
        Add a new contact to the contact list.
        
        Args:
            name (str): The name of the contact.
            email (str): The email address of the contact.
            time (str): The time to send the greeting message to this contact.
        """
        contact = {
            'name': name,
            'email': email,
            'preferred_time': preferred_time
        }
        self.contacts.append(contact)

    def remove_contact(self, name):
        """
        Remove a contact by name from the contact list.
        
        Args:
            name (str): The name of the contact to be removed.
        
        Raises:
            ValueError: If the contact with the specified name is not found.
        """
        self.contacts = [c for c in self.contacts if c['name'] != name]

    def get_contacts(self):
        """
        Retrieve the list of all contacts.
        
        Returns:
            list: A list of dictionaries containing contact details.
        """
        return self.contacts

    def list_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}")
