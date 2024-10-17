import unittest
from morning_greetings.message_sender import send_message
from morning_greetings.contacts_manager import ContactsManager
from morning_greetings.message_generator import generate_message
import os

class TestMessageSender(unittest.TestCase):
    def test_send_message_invalid_email(self):
        """
        Test sending a message with an invalid email address.
        """
        with self.assertRaises(ValueError):
            send_message("invalid-email", "Hello")

    def test_send_message_empty_message(self):
        """
        Test sending a message with an empty message body.
        """
        with self.assertRaises(ValueError):
            send_message("test@example.com", "")

class TestContactsManager(unittest.TestCase):
    def setUp(self):
        """
        Backup and clear the log file before each test.
        """
        self.log_file_path = os.path.join(os.path.dirname(__file__), 'message_log.txt')
        if os.path.exists(self.log_file_path):
            os.rename(self.log_file_path, self.log_file_path + '.bak')

    def tearDown(self):
        """
        Restore the original log file after each test.
        """
        if os.path.exists(self.log_file_path + '.bak'):
            os.rename(self.log_file_path + '.bak', self.log_file_path)

    def test_add_contact(self):
        """
        Test adding a new contact to the contacts list.
        """
        manager = ContactsManager()
        initial_count = len(manager.get_contacts())
        manager.add_contact("Test User", "test@example.com", "08:00 AM")
        self.assertEqual(len(manager.get_contacts()), initial_count + 1)

if __name__ == "__main__":
    unittest.main()