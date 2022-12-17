###############################
# CREATING THE EMAIL MESSAGE
###############################

from email.message import EmailMessage

message = EmailMessage()

# Set the addresses below before sending a message.

sender = "sample@hotmail.com"
recipient = "sample@hotmail.com"

message['From'] = sender
message['To'] = recipient

message['Subject'] = "Greetings from {} to {}!".format(sender, recipient)
body = """Howdy!

Sending emails with Python!"""

message.set_content(body)

# print(message)


###############
# ATTACHMENTS
###############

import os.path
import mimetypes

attachment_path = "/workspaces/Coursera-Google-IT-Automation/Automating-With-Python/IMG_1020s.png"
attachment_filename = os.path.basename(attachment_path)

mime_type, _ = mimetypes.guess_type(attachment_path)

# print(mime_type)

mime_type, mime_subtype = mime_type.split('/', 1)

# print(mime_type)
# print(mime_subtype)

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
        maintype = mime_type,
        subtype = mime_subtype,
        filename = os.path.basename(attachment_path))

# print(message)


########################
# CONNECTING TO SERVER
########################

import smtplib
import getpass

mail_server = smtplib.SMTP('smtp-mail.outlook.com', 587)
mail_server.set_debuglevel(1)

# Interactively get password without saving it in script or printing it to screen
mail_pass = getpass.getpass("Password: ")

mail_server.ehlo()
mail_server.starttls()

mail_server.login(sender, mail_pass)

mail_server.send_message(message)

mail_server.quit()