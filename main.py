import csv
from datetime import datetime


class CSV:
    # Class reads CSV and appends objects to list, removes None objects
    csv_list = list()
    with open("csv_data20223.csv", "r") as f:
        r = csv.reader(f, delimiter=",")
        for sublist in r:
            sublist = list(filter(None, sublist))
            if ' ' in sublist:
                sublist.remove(" ")
            csv_list.append(sublist)


class Date(CSV):
    # Class changes string dates to datetime objects
    for sublist in CSV.csv_list:
        for object in sublist:
            if object is not sublist[0]:
                object = datetime.strptime(object, '%Y/%m/%d')


class Dictionary(CSV):
    # Class removes school names and appends to separate list
    school_names = list()
    for sublist in CSV.csv_list:
        school_names.append(sublist[0])
        sublist.remove(sublist[0])
    # Class assigns key-value pairs (school, dates) using school_names
    visits = dict(zip(school_names,CSV.csv_list))


