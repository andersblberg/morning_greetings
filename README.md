# Morning Greetings

Morning Greetings is a Python package designed to send personalized "Good Morning" messages to a list of contacts. It automates greeting messages, providing a friendly start to your contacts' day.

## Features
- **Automated Greeting Messages**: Schedule daily "Good Morning" messages.
- **Contact Management**: Add, remove, and manage contacts easily.
- **Logging**: Track sent messages in a log file.
- **Customizable Schedule**: Adjust message-sending times.

## Installation

Clone the repository and install it in editable mode:

```sh
git clone https://github.com/andersblberg/morning_greetings.git
cd morning_greetings
pip install -e .
```

## Dependencies
Make sure you have the following dependencies installed:
- **schedule**: To schedule greeting messages.
- **setuptools**: For package setup and installation.

These will be installed automatically during setup.

## Usage

Run the main script to send greetings:

```sh
python main.py
```

By default, greetings are sent at **8:00 AM** each day. You can adjust this in the script to test functionality more frequently. But in the main.py there is a commented section for test purposes where the messages are sent every 10 seconds instead of only 08:00 AM.
### Running for **08:00 AM **

```python
# Schedule the greetings to be sent every day at 8:00 AM
schedule.every().day.at("08:00").do(send_morning_greetings)

# Keep the script running and checking the schedule
while True:
    schedule.run_pending()
    time.sleep(60)
```

### Running for Testing Purposes
Modify the schedule to send greetings every 10 seconds instead of daily:

```python
# Schedule the greetings to be sent every 10 seconds for test case
schedule.every(10).seconds.do(send_morning_greetings)


# Keep the script running and checking the schedule every 5 second for test case
while True:
    schedule.run_pending()
    time.sleep(5)
```

## Running Tests
The `test.py` file includes unit tests for key components. Run the tests using:

```sh
python test.py
```

The tests validate features like adding contacts, sending messages, and proper error handling.

## Project Structure

- **main.py**: Main script to send greetings.
- **morning_greetings/**: Package directory:
  - **contacts.py**: Manages contact information.
  - **contacts_manager.py**: Handles adding, removing, and fetching contacts.
  - **message_generator.py**: Generates greeting messages.
  - **message_sender.py**: Sends messages.
  - **logger.py**: Logs sent messages.
- **test.py**: Unit tests for the project.
- **message_log.txt**: Logs details of sent messages.

## Future Improvements
- **Message Customization**: Support varied and personalized greeting templates.
- **User Interface**: Develop a GUI for easier management.
- **Configurable Scheduling**: Allow users to configure schedules without editing the script.

## Contributing

Contributions are welcome! Submit a pull request or open an issue for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Contact

For questions or suggestions, feel free to contact:
- **Author**: Anders Blomberg
- **Email**: s339872@oslomet.no
- **GitHub**: [andersblberg](https://github.com/andersblberg)

