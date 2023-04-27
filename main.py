import csv


class CSV:
    # Class CSV reads CSV file and adds key-value pairs to visits dictionary
    visits = dict()
    with open("csv_data20223.csv", "r") as f:
        r = csv.reader(f, delimiter=",")
        for sublist in r:
            # None objects and blank strings are removed
            sublist = list(filter(None, sublist))
            if ' ' in sublist:
                sublist.remove(" ")
            # First object contains name of school and is reused for key
            visits[str(sublist[0])] = sublist


class Dates(CSV):
    print(CSV.visits)
