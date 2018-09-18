def checkWeekDay(day):
  if day == "Monday":
    return True
  elif day == "Tuesday":
    return True
  elif day == "Wednesday":
    return True
  elif day == "Thursday":
    return True
  elif day == "Friday":
    return True
  else:
    return False
    
def checkVacation(vacation):
  if vacation == "yes":
    return True
  else:
    return False

def sleep_in(weekday, vacation):
  if checkWeekDay(weekday) and checkVacation(vacation):
    print("you can go sleep all you want")
    return True
  elif checkWeekDay(weekday) and not checkVacation(vacation):
    print("This is not a vacation!!!! Go to work!")
    return False
  elif not checkWeekDay(weekday) and checkVacation(vacation):
    print("Enjoy your vacation.....yaaaaawn")
    return True

day = input("What day is it?")
vacation = input("Are you on vacation? yes or no")

#day = "Saturday"
#vacation = "yes"

sleep_in(day, vacation)