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
            # First object contains name of school and is reused for key
            visits[(sublist[0])] = sublist
    print(visits)
