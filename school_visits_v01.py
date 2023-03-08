#Dates follow: Year/Month/Day
class Date:
    def __init__(self,y,m,dy):
        self.year = y
        self.month = m
        self.day = dy
        
    def __repr__(self):
        return((str(self.year))+"/"+(str(self.month))+"/"+(str(self.day)))

d1 = Date(2022,8,10)

#School names have been changed for privacy

class Visits(Date):
    u = "Uma High School"
    k = "Kaze High School"
    y = "Yuki High School"
    def __init__(self,s,dt):
        self.school = s
        self.date = dt

    def __repr__(self):
        return("You will visit "+(self.school)+" on "+(str(self.date)))

s1 = Visits(Visits.u,d1)

print(s1)
