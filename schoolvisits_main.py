#School names changed for privacy
import csv

#Dates recorded on an CSV file
class Data():
    with open("sv_data.csv","r") as f:
        visits = {}
        r = csv.reader(f, delimiter=",")
        for row in r:
            if "Yuki" in row:
                visits["Yuki"] = row
            elif "Kaze" in row:
                visits["Kaze"] = row
            elif "Uma" in row:
                visits["Uma"] = row
        visits["Yuki"].remove("Yuki")
        visits["Kaze"].remove("Kaze")
        visits["Uma"].remove("Uma")

class User(Data):
    print("This program is for tracking ALT school visits in Hokkaido")
    loop_1 = True
    while loop_1 == True:
        question_1 = input("""
Would you like to know about:
1. Number of visits
2. Completed visits
3. Upcoming visits: """)
        question_1 = question_1.lower()
        if question_1 in ["1", "one","number of visits"]:
            print("one")
        elif question_1 in ["2","two","completed visits"]:
            print("two")
        elif question_1 in ["3","three","upcoming visits"]:
            print("three")
        else:
            print("I can't accept that input")

        
