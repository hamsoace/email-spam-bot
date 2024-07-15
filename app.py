from flask import Flask, render_template, request, url_for, flash
import smtplib
import datetime
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)

def get_contacts(file):
    emails = []
    print("File contents:")
    for line in file.readlines():
        line = line.decode('utf-8').strip()
        print(line)
        if '@' in line:
            emails.append(line)
    print(f"Emails read from file: {emails}")
    return emails
    
def sendEmail(message_template, sender, password, email):
    try:
        date = datetime.datetime.now().strftime("%A, %B %d, %Y %I:%M:%S %p")
        message = message_template.format(DATE = date)
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login(sender, password)
        s.sendmail(sender, email, message.encode('utf-8'))
        s.quit()
        return True
    except Exception as e:
        print(f"Error sending email to {email}: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        print(f"Error sending email to {email}: {str(e)}")
        return False

@app.route('/', methods =['GET', 'POST'])
def index():
    if request.method == 'POST':
        sender = request.form['sender']
        password = request.form['password']
        subject = request.form['subject']
        message_body = request.form['message']
        contacts_file = request.files['contacts']

        print(f"Sender: {sender}")  # Debug print
        print(f"Subject: {subject}")  # Debug print
        print(f"Message body: {message_body}")  # Debug print
        print(f"Contacts file: {contacts_file.filename}")

        if contacts_file.filename == '':
            flash('No file selected', 'error')
            return render_template('index.html')

        contacts_file.stream.seek(0)

        message_template = f"""Subject: {subject}
Hello,

This email was sent on {{DATE}}.

Message: {message_body}

Best regards,
Yours"""
        emails = get_contacts(contacts_file)
        print(f"Number of emails to send: {len(emails)}")

        success_count = 0
        for email in emails:
            if sendEmail(message_template, sender, password, email.strip()):
                success_count += 1
                print(f"Email sent to {email}")
            else:
                print(f"Failed to send to {email}")

        if success_count == len(emails):
            flash(f"All emails sent successfully! ({success_count}/{len(emails)})", "success")
        elif success_count > 0:
            flash(f"Partially successful. Sent {success_count} out of {len(emails)} emails.", "warning")
        else:
            flash("Failed to send any emails. Please check your credentials and try again.", "error")
        
        if contacts_file.filename == '':
            flash('No file selected', 'error')
            return render_template('index.html')
    
    return render_template('index.html')
  
if __name__ == '__main__':
    app.run(debug=True)