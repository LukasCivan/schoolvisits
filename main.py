import csv
from datetime import datetime


class CSV:
    # Class reads CSV, converts to datetime objects, and adds to dictionary
    visits = dict()
    with open("csv_data20223.csv", "r") as f:
        r = csv.reader(f, delimiter=",")
        for sublist in r:
            # None objects and blank strings are removed
            sublist = list(filter(None, sublist))
            if ' ' in sublist:
                sublist.remove(" ")
            for object in sublist:
                # Dates are changed from strings to date objects
                if object is not sublist[0]:
                    object = datetime.strptime(object, '%Y/%m/%d')
            visits[(sublist[0])] = sublist
    print(visits)


class Operations(CSV):
    # Class contains all functions that will be used wih the user interface
    # Returns total number of visits
    count = 0
    for key in CSV.visits:
        if isinstance(CSV.visits[key], list):
            # Filters out school names
            count += len(CSV.visits[key])
    print(count)
