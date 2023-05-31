import csv
from datetime import datetime
from datetime import date


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
    # Class creates dictionary, keys = dates and values = school names
    school_names = list()
    for sublist in CSV.csv_list:
        school_names.append(sublist[0])
    visits = dict()
    for list in CSV.csv_list:
        for item in list:
            if item in school_names:
                pass
            else:
                visits[item] = list[0]
    print(visits)


class User(Dictionary):
    # Class produces printed message for user
    # Establishes today's date as today variable
    today_un_formatted = date.today()
    today = today_un_formatted.strftime('%Y/%-m/%d')
    if today in Dictionary.visits:
        today_visit = "a school visit today"
    else:
        today_visit = "no visits today."
    # Establishes if there is a school visit today
    print(
        "Welcome to the School Visits Project\n"
        "There are", len(Dictionary.school_names), "schools and",
        len(Dictionary.visits), "visits.\nYou have", today_visit,
    )
