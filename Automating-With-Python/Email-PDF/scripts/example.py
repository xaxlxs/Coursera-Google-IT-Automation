#!/usr/bin/env python3

import emails
import os
import reports

table_data=[
    ['Name', 'Amount', 'Value'],
    ['elderberries', 10, 0.45],
    ['figs', 5, 3],
    ['apples', 4, 2.75],
    ['durians', 1, 25],
    ['bananas', 5, 1.99],
    ['cherries', 23, 5.80],
    ['grapes', 13, 2.48],
    ['kiwi', 4, 0.49]]

# Original example
# reports.generate("/tmp/report.pdf", "A Complete Inventory of My Fruit", "This is all my fruit.", table_data)

# sender = "sender@example.com"
# receiver = "{}@example.com".format(os.environ.get('USER'))

# My details
reports.generate("/workspaces/Coursera-Google-IT-Automation/Automating-With-Python/Email-PDF/report.pdf", "A Complete Inventory of My Fruit", "This is all my fruit.", table_data)

sender = "example@example.com"
receiver = "example@example.com"


subject = "List of Fruits"
body = "Hi\n\nI'm sending an attachment with all my fruit."

# Original example
# message = emails.generate(sender, receiver, subject, body, "/tmp/report.pdf")

# My details
message = emails.generate(sender, receiver, subject, body, "/workspaces/Coursera-Google-IT-Automation/Automating-With-Python/Email-PDF/report.pdf")
emails.send(message)
