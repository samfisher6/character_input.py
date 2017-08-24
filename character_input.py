import datetime
from datetime import timedelta

now = datetime.datetime.now()

def hello_person():
    global now
    name = raw_input("What is your name?")
    age = int(raw_input("how old are you ?"))
    print "hello " +str(name) + " you are "+ str(age)+" years old"
    year_of_100 = 100 - age
    diff = datetime.timedelta(days = 365 * (int(year_of_100)))
    print
    print "you will turn 100 in " + str(year_of_100) + " years"
    print
    print "since today is "+ str(now.isoformat())
    future = now + diff
    print "that will be on " + str(future.strftime("%m/%d/%Y"))

print hello_person()
