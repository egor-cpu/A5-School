import random
from datetime import datetime, timedelta

def generateRandomDates():
    dates = []
    start_date = datetime(2000, 1, 1)
    end_date = datetime(2023, 12, 31)
    
    for _ in range(100):
        random_days = random.randint(0, (end_date - start_date).days)
        random_date = start_date + timedelta(days = random_days)
        dates.append(random_date)
    
    return dates

def getNearestDate(targetDate, leftDate, rightDate):
    leftDelta = abs(targetDate - leftDate).days
    rightDelta = abs(targetDate - rightDate).days
    if leftDelta < rightDelta:
        return leftDate
    else:
        return rightDate


def findNearestAndFurthestDates(dates, targetDate):
    if dates and targetDate == None:
        return Exception("ArgumentNullException in findNearestAndFurthestDates")
    
    nearestDate = None
    furtherDate = None

    if targetDate not in dates:
        dates.append(targetDate)
    dates.sort()  
    print(dates) #For checking!!!!!

    targetDateIndex = dates.index(targetDate)
    datesLastIndex = len(dates) - 1

    if targetDateIndex == datesLastIndex:
        nearestDate = dates[targetDateIndex - 1]
        furtherDate = dates[targetDateIndex]   
         
    elif targetDateIndex == 0:
       nearestDate = dates[targetDateIndex + 1]
       furtherDate = dates[datesLastIndex]  
    else:
        nearestDate = getNearestDate(targetDate, dates[targetDateIndex - 1], dates[targetDateIndex + 1])
        furtherDate = dates[datesLastIndex]

    return nearestDate.strftime("%Y %m %d"), furtherDate.strftime("%Y %m %d")


userInputDate = input("Your date (like 'year month day'): ")
datetimeObject = datetime.strptime(userInputDate, '%Y %m %d')

print("You input: ", datetimeObject)
print(f"nearestDate, furtherDate = {(findNearestAndFurthestDates(generateRandomDates(), None))}")