#!/usr/bin/env python3

import json
import locale
import sys

def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def format_car(car):
    """Given a car dictionary, returns a nicely formatted name."""
    return "{} {} ({})".format(
            car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
    """Analyzes the data, looking for maximums.

    Returns a list of lines that summarize the information.
    """
    max_revenue = {"revenue": 0}
    for item in data:
        # Calculate the revenue generated by this model (price * total_sales)
        # We need to convert the price from "$1234.56" to 1234.56
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price
        if item_revenue > max_revenue["revenue"]:
            item["revenue"] = item_revenue
            max_revenue = item

        # TODO: also handle max sales
    
    max_sales = {"total_sales": 0}
    for item in data:
        if item["total_sales"] > max_sales["total_sales"]:
            max_sales = item

        # TODO: also handle most popular car_year

    year_sales = {}
    for item in data:
        if item["car"]["car_year"] not in year_sales:
            year_sales[item["car"]["car_year"]] = 0
        year_sales[item["car"]["car_year"]] += item["total_sales"]

    highest_year = [0, 0]
    for k, v in year_sales.items():
        if v > highest_year[1]:
            highest_year = [k, v]

    summary = [
        "The {} generated the most revenue: ${}".format(
            format_car(max_revenue["car"]), max_revenue["revenue"]),
        # Add max sales and most popular car_year
        "The {} had the most sales: {}".format(
            format_car(max_sales["car"]), max_sales["total_sales"]),
        "The most popular year was {} with {} sales.".format(
            highest_year[0], highest_year[1])
    ]

    return summary


def cars_dict_to_table(car_data):
    """Turns the data in car_data into a list of lists."""
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in car_data:
        table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
    return table_data


def main(argv):
    """Process the JSON data and generate a full report out of it."""
    
    # Original example
    # data = load_data("car_sales.json")

    # My informaton
    data = load_data("/workspaces/Coursera-Google-IT-Automation/Automating-With-Python/Email-PDF/car_sales.json")


    summary = process_data(data)
    print(summary)

    # TODO: turn this into a PDF report

    import reports
    reports.generate(
        "/workspaces/Coursera-Google-IT-Automation/Automating-With-Python/Email-PDF/cars.pdf", 
        "Sales summary for last month", 
        "<br/>".join(summary), 
        cars_dict_to_table(data))

    # TODO: send the PDF report as an email attachment



if __name__ == "__main__":
    main(sys.argv)
