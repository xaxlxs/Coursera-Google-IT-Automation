#!/usr/bin/env python3

import sys
import os
import glob
from datetime import datetime
import reports

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
            paragraph += "name: " + name + "\n" + "weight: " + weight + "\n\n"
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



if __name__ == "__main__":
    main(sys.argv)