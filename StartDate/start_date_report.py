#!/usr/bin/env python3

import csv
import datetime
from distutils import file_util
import requests


FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_employees(url, start_date):
    response = requests.get(url, stream=True)
    lines = []
    employees = []
    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    reader = csv.reader(lines[1:])
    for line in reader:
        row_date = datetime.datetime.strptime(line[3], '%Y-%m-%d')
        if row_date > start_date:
            employees.append("{},{} {}".format(line[3], line[0], line[1]))
    employees.sort()

    hired_date = ""
    hired_on = []
    for i in employees:
        date = datetime.datetime.strptime(i[:10], '%Y-%m-%d')
        name = i[11:]
        if hired_date == "":
            hired_date = date
            hired_on.append(name)
        else:
            if hired_date == date:
                hired_on.append(name)
            else:
                print("Started on {}: {}".format(hired_date.strftime("%b %d, %Y"), hired_on))
                hired_date = date
                hired_on = []
                hired_on.append(name)

def main():
    start_date = get_start_date()
    get_employees(FILE_URL, start_date)

if __name__ == "__main__":
    main()



'''
PSUDO CODE:
ask for date
dowload file
if row date greater than input date and less than today
append date, name to list
sort list
print formatted text
'''
