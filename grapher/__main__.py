import argparse
from datetime import datetime
from grapher import DATE_FORMAT, fetch_data, filter_data, draw_chart
import re

if __name__ == "__main__":
    # check for user arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("start_date")
    parser.add_argument("end_date")
    args = parser.parse_args()
    print(args.start_date, args.end_date)

    # check argument if it is in the correct
    # ^(([0-3]{1})([0-9]{1}))-(([0-1]{1})([1-9]{1}))-(([0-9]{4}))$
    regex = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"
    error_message = "acceptable format is 'dd-mm-yy' day must be 2 digits and not greater than 31 or 00, month must be 2 digits and not greater than 12 or 00"
    if not re.match(regex, args.start_date):
        raise ValueError("InValid date format for start_date: " + error_message)
    if not re.match(regex, args.end_date):
        raise ValueError("InValid date format for end_date: " + error_message)
    # fetch the data
    d = fetch_data()
    labels = list(d.keys())
    data = [[value] for value in d.values()]
    start_date = datetime.strptime(args.start_date, DATE_FORMAT)
    end_date = datetime.strptime(args.end_date, DATE_FORMAT)
    data, labels = filter_data(data, labels, start_date, end_date)
    # plot the points
    if len(labels) > 0:
        draw_chart(data, labels, title=f"Graph of Number of Users from {start_date} to {end_date}")
    else:
        print("No data between the specified date")
