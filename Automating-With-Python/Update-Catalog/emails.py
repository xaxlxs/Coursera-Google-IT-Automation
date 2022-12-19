#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

def generate_email(sender, recipient, subject, body, attachment=None):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # Process the attachment and add it to the email
    if attachment != None:
        attachment_filename = os.path.basename(attachment)
        mime_type, _ = mimetypes.guess_type(attachment)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(attachment, 'rb') as ap:
            message.add_attachment(ap.read(),
                                maintype=mime_type,
                                subtype=mime_subtype,
                                filename=attachment_filename)
    return message

def send_email(message):
    # Original details
    # mail_server = smtplib.SMTP('localhost')
    # mail_server.send_message(message)
    # mail_server.quit()
    
    # My connection details

    import getpass
    # sender = "sample@sample.com"

    mail_server = smtplib.SMTP('smtp-mail.outlook.com', 587)

    # Interactively get password without saving it in script or printing it to screen
    mail_pass = getpass.getpass("Password: ")

    mail_server.ehlo()
    mail_server.starttls()

    mail_server.login(message["From"], mail_pass)

    mail_server.send_message(message)
    mail_server.quit()