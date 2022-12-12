#! /usr/bin/env python3

import os
import json
import requests

address = "http://<corpweb-external-IP>/feedback"
relative_path = "data/feedback"
source = os.path.join(os.getcwd(), relative_path)

for file in os.listdir(source):
    with open(os.path.join(source, file)) as reader:
        title, name, date, review = reader.readlines()
        dict = {"title": title.strip(), "name": name.strip(), "date": date.strip(), "feedback": review.strip()}
        print(dict)

        response = requests.post(address, data=dict)
        print(response.status_code)