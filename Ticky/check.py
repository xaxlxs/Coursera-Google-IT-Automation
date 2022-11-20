'''
Create 2 reports
1 list of all errors and the number of times they appear, sorted highest to lowest
1 list of all users and the number of info and number of error messages sorted by username
error type = match group 1
message = match group 2
username = match group 3
'''

import re
import operator
import csv

logfile = 'Ticky/log.txt'
errorreport = "Ticky/errors.csv"
userreport = "Ticky/users.csv"

errors = {}
users = {}

with open(logfile) as file:
    for line in file:
        match = re.search(r"ticky: ([\w]*):? ([\w' ]*) [\[[0-9#]*\]?]? ?\((.*)\)$", line)
        if match.group(1) == "ERROR":
            if match.group(2) not in errors:
                errors[match.group(2)] = 0
            errors[match.group(2)] += 1
        if match.group(3) not in users:
            users[match.group(3)] = [0, 0]
            # users[match.group(3)] = {}
            # users[match.group(3)]["ERROR"] = 0
            # users[match.group(3)]["INFO"] = 0
        if match.group(1) == "ERROR":
            users[match.group(3)][1] += 1
        if match.group(1) == "INFO":
            users[match.group(3)][0] += 1

errors = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)
users = sorted(users.items())

errors.insert(0, ("Error", "Count"))
users.insert(0, ("Username", ["INFO", "ERROR"]))

# errors = dict(errors)
# users = dict(users)

# print(errors)
# print(users)

# for line in users:
#     print(line[1][0])

with open(errorreport, "w", newline='') as file:
    for line in errors:
        file.write(str(line[0])+","+str(line[1])+"\n")

with open(userreport, 'w', newline='') as file:
    for line in users:
        file.write(str(line[0])+","+str(line[1][0])+","+str(line[1][1])+"\n")
