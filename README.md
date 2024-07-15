# Bulk Email Sender

## Description
Bulk Email Sender is a Flask-based web application that allows users to send personalized emails to multiple recipients simultaneously. This application is perfect for sending newsletters, announcements, or any mass communication where personalization is key.

## Features
- User-friendly web interface
- Bulk email sending capability
- Customizable email subject and body
- Supports uploading a contact list file
- Real-time feedback on email sending status

## Requirements
- Python 3.7+
- Flask
- smtplib (comes with Python standard library)

## Installation
1. Clone this repository:
[text](https://github.com/hamsoace/email-spam-bot.git)
2. Navigate to the project directory:
    cd email-spam-bot
3. Install the required packages:
    pip install -r requirements.txt

## Usage
1. Run the Flask application:
python app.py
2. Open a web browser and go to `http://localhost:5000`
3. Fill in the form with the following information:
- Sender Email: Your Gmail address
- Password: Your Gmail password or app-specific password
- Subject: The subject line for your emails
- Message: The body of your email
- Contacts File: Upload a text file with email addresses (one per line)
4. Click "Send Emails" to start the sending process

## Contact File Format
The contacts file should be a plain text file with one email address per line. For example:
    john@example.com
    jane@example.com
    user@domain.com

## Security Note
This application requires your Gmail credentials. It's recommended to use an app-specific password instead of your main account password. You can create an app-specific password in your Google Account settings.

## Limitations
- Currently only supports Gmail as the sending server
- Designed for personal or small-scale use
- May be subject to Gmail's sending limits

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/hamsoace/email-spam-bot.git/issues) if you want to contribute.

## License
[MIT](https://choosealicense.com/licenses/mit/)