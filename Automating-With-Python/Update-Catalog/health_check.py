#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails

sender = "automation@example.com"
recipient = "username@example.com"
subject = ""
body = "Please check your system and resolve the issue as soon as possible."

# Check if CPU usage is over 80%
if psutil.cpu_percent(1) > 80:
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_email(sender, recipient, subject, body)
    emails.send_email(message)

# Check if available disk space is below 20%
total, used, free = shutil.disk_usage("./") 
if free / total < 0.2:
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_email(sender, recipient, subject, body)
    emails.send_email(message)

# Check if available memory is less than 500MB
if psutil.virtual_memory()[1]/1000000 < 500:
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_email(sender, recipient, subject, body)
    emails.send_email(message)

# Check if hostname 'localhost' cannot be resolved to '127.0.0.1'
host = socket.gethostbyname('localhost')
if host != "127.0.0.1":
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_email(sender, recipient, subject, body)
    emails.send_email(message)