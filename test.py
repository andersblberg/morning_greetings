import unittest
from morning_greetings.logger import log_message
import os

LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), "message_log.txt")

class TestLogger(unittest.TestCase):
    def test_log_message(self):
        # Clear existing log if it exists for clean testing
        if os.path.exists(LOG_FILE_PATH):
            os.remove(LOG_FILE_PATH)
        
        contact = {'name': 'Alice', 'contact_info': 'alice@example.com', 'preferred_time': '08:00 AM'}
        log_message(contact, "Good Morning, Alice")

        # Verify that the log entry was written to message_log.txt
        with open(LOG_FILE_PATH, "r") as log_file:
            logs = log_file.read()
            self.assertIn("Alice", logs)
            self.assertIn("Good Morning, Alice", logs)

    def tearDown(self):
        # Clean up log file after tests
        if os.path.exists(LOG_FILE_PATH):
            os.remove(LOG_FILE_PATH)

if __name__ == "__main__":
    unittest.main()
