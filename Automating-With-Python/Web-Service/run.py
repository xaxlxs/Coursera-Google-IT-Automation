#! /usr/bin/env python3

import os
import json
import requests

address = "http://<corpweb-external-IP>/feedback"
relative_path = "data/feedback"
source = os.path.join(os.getcwd(), relative_path)

# os.chdir("..")
# os.chdir("..")

# to get script to work on qwiklabs, uncomment 2 chdir commands above, change source belot to relative_path

for file in os.listdir(source):
    with open(os.path.join(source, file)) as reader:
        title, name, date, review = reader.readlines()
        dict = {"title": title.strip(), "name": name.strip(), "date": date.strip(), "feedback": review.strip()}
        review_json = json.dumps(dict)
        # print(review_json)

        response = requests.post(address, json=dict)
        print(response.status_code)