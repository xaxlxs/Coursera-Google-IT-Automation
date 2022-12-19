#!/usr/bin/env python3

import sys
import os
import glob
from datetime import datetime
import reports
import emails

# Verify source location in Qwiklabs
source = "supplier-data/descriptions/"

def process_data():
    paragraph = ""
    for file in glob.glob("*.txt", root_dir=source):
        with open(source + file) as reader:
            # print(reader.readlines())
            name = reader.readline().strip()
            weight = reader.readline().strip()
            # print(name, weight)
            paragraph += "<br/>" + "name: " + name + "<br/>" + "weight: " + weight + "<br/>"
    return paragraph



def main(argv):
    data = process_data()
    # print(data)

    # Update attachment path in Qwiklab: /tmp/processed.pdf
    attachment = "processed.pdf"

    today = datetime.now()
    date = today.strftime("%B %d, %Y")

    title = "Processed Update on " + date
    reports.generate_report(attachment, title, data)

    message = emails.generate_email(
        "automation@example.com",
        "username@example.com",
        "Upload Completed - Online Fruit Store",
        "All fruits are uploaded to our website successfully. A detailed list is attached to this email",
        attachment
    )

    emails.send_email(message)

if __name__ == "__main__":
    main(sys.argv)