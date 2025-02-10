hrsMon = 0
hrsTues = 0
hrsWed = 0
hrsThurs = 0
hrsFri = 0
hrsSat = 0
hrsSun = 0

name = input("\n\nPlease enter your name: ")
print("\nHello, ", name, "!\n")


Calendar = {
    "1Monday": "0",
    "1Tuesday": "0",
    "1Wednesday": "0",
    "1Thursday": "0",
    "1Friday": "0",
    "1Saturday": "0",
    "1Sunday": "0",
    "2Monday": "0",
    "2Tuesday": "0",
    "2Wednesday": "0",
    "2Thursday": "0",
    "2Friday": "0",
    "2Saturday": "0",
    "2Sunday": "0",
    "3Monday": "0",
    "3Tuesday": "0",
    "3Wednesday": "0",
    "3Thursday": "0",
    "3Friday": "0",
    "3Saturday": "0",
    "3Sunday": "0",
    "4Monday": "0",
    "4Tuesday": "0",
    "4Wednesday": "0",
    "4Thursday": "0",
    "4Friday": "0",
    "4Saturday": "0",
    "4Sunday": "0",
    "5Monday": "0",
    "5Tuesday": "0",
    "5Wednesday": "0",
    "5Thursday": "0",
    "5Friday": "0",
    "5Saturday": "0",
    "5Sunday": "0",
}

Week = {
    "Monday": "0",
    "Tuesday": "0",
    "Wednesday": "0",
    "Thursday": "0",
    "Friday": "0",
    "Saturday": "0",
    "Sunday": "0"
}


def selection():
    return input("What would you like to do?\n 1) View Weekly time"
                 "\n 2) View Pay Period time \n 3) Calendar View \n"
                 " 4) Punch In/Edit Time\n 5) Exit\n")


def weekView(hrsMon, hrsTues, hrsWed, hrsThurs, hrsFri, hrsSat, hrsSun):
    weekHours = (int(hrsMon) + int(hrsTues) + int(hrsWed) + int(hrsThurs)
                 + int(hrsFri) + int(hrsSat) + int(hrsSun))

    print("Monday:    ", hrsMon, " hrs\n"
          "Tuesday:   ", hrsTues, " hrs\n"
          "Wednseday: ", hrsWed, " hrs\n"
          "Thursday:  ", hrsThurs, " hrs\n"
          "Friday:    ", hrsFri, " hrs\n"
          "Saturday:  ", hrsSat, " hrs\n"
          "Sunday:    ", hrsSun, " hrs\n"
          )
    print("You worked:", weekHours, " hours this week\n\n")


def periodView(Calendar):
    period = input("Which pay period for this month would you like to view(1"
                   " or 2)?\n")
    if period == "1":
        print("\nWeek 1\n")
        weekView(Calendar["1Monday"], Calendar["1Tuesday"],
                 Calendar["1Wednesday"], Calendar["1Thursday"],
                 Calendar["1Friday"], Calendar["1Saturday"],
                 Calendar["1Sunday"])
        print("\nWeek 2\n")
        weekView(Calendar["2Monday"], Calendar["2Tuesday"],
                 Calendar["2Wednesday"], Calendar["2Thursday"],
                 Calendar["2Friday"], Calendar["2Saturday"],
                 Calendar["2Sunday"])
    elif period == "2":
        print("\nWeek 3\n")
        weekView(Calendar["3Monday"], Calendar["3Tuesday"],
                 Calendar["3Wednesday"], Calendar["3Thursday"],
                 Calendar["3Friday"], Calendar["3Saturday"],
                 Calendar["3Sunday"])
        print("\nWeek4\n")
        weekView(Calendar["4Monday"], Calendar["4Tuesday"],
                 Calendar["4Wednesday"], Calendar["4Thursday"],
                 Calendar["4Friday"], Calendar["4Saturday"],
                 Calendar["4Sunday"])


def timePunch(Calendar):
    wkInput = input("Which week would you like to enter time for(1,2,3,4,"
                    "5)?\n")
    dayInput = input("Which day of the week(Mon, Tues, Wed, Thurs, Fri,"
                     " Sat, Sun)?\n")
    hrWork = input("How many hours did you work?\n")
    print(wkInput)
    print(dayInput)
    print(hrWork)
    if wkInput == "1":
        if dayInput == 'Mon':
            Calendar["1Monday"] = hrWork
        elif dayInput == "Tues":
            Calendar["1Tuesday"] = hrWork
        elif dayInput == "Wed":
            Calendar["1Wednesday"] = hrWork
        elif dayInput == "Thurs":
            Calendar["1Thursday"] = hrWork
        elif dayInput == "Fri":
            Calendar["1Friday"] = hrWork
        elif dayInput == "Sat":
            Calendar["1Saturday"] = hrWork
        elif dayInput == "Sun":
            Calendar["1Sunday"]
        else:
            print("Invalid input start again.\n")

    elif wkInput == "2":
        if dayInput == "Mon":
            Calendar["2Monday"] = hrWork
        elif dayInput == "Tues":
            Calendar["2Tuesday"] = hrWork
        elif dayInput == "Wed":
            Calendar["2Wednesday"] = hrWork
        elif dayInput == "Thurs":
            Calendar["2Thursday"] = hrWork
        elif dayInput == "Fri":
            Calendar["2Friday"] = hrWork
        elif dayInput == "Sat":
            Calendar["2Saturday"] = hrWork
        elif dayInput == "Sun":
            Calendar["2Sunday"]
        else:
            print("Invalid input start again.\n")

    elif wkInput == "3":
        if dayInput == "Mon":
            Calendar["3Monday"] = hrWork
        elif dayInput == "Tues":
            Calendar["3Tuesday"] = hrWork
        elif dayInput == "Wed":
            Calendar["3Wednesday"] = hrWork
        elif dayInput == "Thurs":
            Calendar["3Thursday"] = hrWork
        elif dayInput == "Fri":
            Calendar["3Friday"] = hrWork
        elif dayInput == "Sat":
            Calendar["3Saturday"] = hrWork
        elif dayInput == "Sun":
            Calendar["3Sunday"]

    elif wkInput == "4":
        if dayInput == "Mon":
            Calendar["4Monday"] = hrWork
        elif dayInput == "Tues":
            Calendar["4Tuesday"] = hrWork
        elif dayInput == "Wed":
            Calendar["4Wednesday"] = hrWork
        elif dayInput == "Thurs":
            Calendar["4Thursday"] = hrWork
        elif dayInput == "Fri":
            Calendar["4Friday"] = hrWork
        elif dayInput == "Sat":
            Calendar["4Saturday"] = hrWork
        elif dayInput == "Sun":
            Calendar["4Sunday"]
        else:
            print("Invalid input start again.\n")

    elif wkInput == "5":
        if dayInput == "Mon":
            Calendar["5Monday"] = hrWork
        elif dayInput == "Tues":
            Calendar["5Tuesday"] = hrWork
        elif dayInput == "Wed":
            Calendar["5Wednesday"] = hrWork
        elif dayInput == "Thurs":
            Calendar["5Thursday"] = hrWork
        elif dayInput == "Fri":
            Calendar["5Friday"] = hrWork
        elif dayInput == "Sat":
            Calendar["5Saturday"] = hrWork
        elif dayInput == "Sun":
            Calendar["5Sunday"]
        else:
            print("Invalid input start again.\n")


while True:

    menuSel = selection()
    if menuSel == "1":
        selector = input("Which weeks time would you like to see"
                         "(1,2,3,4,5)?\n")
        if selector == "1":
            weekView(Calendar["1Monday"], Calendar["1Tuesday"],
                     Calendar["1Wednesday"], Calendar["1Thursday"],
                     Calendar["1Friday"], Calendar["1Saturday"],
                     Calendar["1Sunday"])
        if selector == "2":
            weekView(Calendar["2Monday"], Calendar["2Tuesday"],
                     Calendar["2Wednesday"], Calendar["2Thursday"],
                     Calendar["2Friday"], Calendar["2Saturday"],
                     Calendar["2Sunday"])
        if selector == "3":
            weekView(Calendar["3Monday"], Calendar["3Tuesday"],
                     Calendar["3Wednesday"], Calendar["3Thursday"],
                     Calendar["3Friday"], Calendar["3Saturday"],
                     Calendar["3Sunday"])
        if selector == "4":
            weekView(Calendar["4Monday"], Calendar["4Tuesday"],
                     Calendar["4Wednesday"], Calendar["4Thursday"],
                     Calendar["4Friday"], Calendar["4Saturday"],
                     Calendar["4Sunday"])
        if selector == "5":
            weekView(Calendar["5Monday"], Calendar["5Tuesday"],
                     Calendar["5Wednesday"], Calendar["5Thursday"],
                     Calendar["5Friday"], Calendar["5Saturday"],
                     Calendar["5Sunday"])
        """#print(" weekly View code")"""
    elif menuSel == "2":
        periodView(Calendar)
    elif menuSel == "3":
        print("Week 1:\n")
        weekView(Calendar["1Monday"], Calendar["1Tuesday"],
                 Calendar["1Wednesday"], Calendar["1Thursday"],
                 Calendar["1Friday"], Calendar["1Saturday"],
                 Calendar["1Sunday"])
        print("Week 2:\n")
        weekView(Calendar["2Monday"], Calendar["2Tuesday"],
                 Calendar["2Wednesday"], Calendar["2Thursday"],
                 Calendar["2Friday"], Calendar["2Saturday"],
                 Calendar["2Sunday"])
        print("Week 3:\n")
        weekView(Calendar["3Monday"], Calendar["3Tuesday"],
                 Calendar["3Wednesday"], Calendar["3Thursday"],
                 Calendar["3Friday"], Calendar["3Saturday"],
                 Calendar["3Sunday"])
        print("Week 4:\n")
        weekView(Calendar["4Monday"], Calendar["4Tuesday"],
                 Calendar["4Wednesday"], Calendar["4Thursday"],
                 Calendar["4Friday"], Calendar["4Saturday"],
                 Calendar["4Sunday"])
        print("Week 5:\n")
        weekView(Calendar["5Monday"], Calendar["5Tuesday"],
                 Calendar["5Wednesday"], Calendar["5Thursday"],
                 Calendar["5Friday"], Calendar["5Saturday"],
                 Calendar["5Sunday"])

    elif menuSel == "4":
        timePunch(Calendar)
    elif menuSel == "5":
        """prompt for selection again"""
        exit = input("are you sure you want to exit the program? (y/n)")
        if exit == "y":
            quit()
