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
    # Class removes school names and appends to separate list
    school_names = list()
    for sublist in CSV.csv_list:
        school_names.append(sublist[0])
        sublist.remove(sublist[0])
    # Class assigns key-value pairs (school, dates) using school_names
    visits = dict(zip(school_names, CSV.csv_list))


class User(Dictionary):
    # Class produces printed message for user
    # Establishes today's date
    today_unformatted = date.today()
    today = today_unformatted.strftime('%Y/%m/%d')
    # Establishes if there is a visit today
    visit_today = ()
    for key in Dictionary.visits:
        for value in key:
            if value == today:
                visit_today = "There is a visit today"
                key = "at", today_school,"."
            else:
                visit_today = "There are no visits today."
                key = "You can rest!"
    print(
        "Welcome to the School Visits Project \n\n",
        visit_today, key
    )

