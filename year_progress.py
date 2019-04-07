import calendar
import datetime

def getDates():

    currentDateTime = datetime.datetime.now()
    currentDay = currentDateTime.day 
    currentMonth = currentDateTime.month
    currentYear = currentDateTime.year
    
    return ({'currentDay':currentDay, 'currentMonth':currentMonth ,'currentYear':currentYear })

def getNumberOfDaysElapsed(day, month, year):

    totalOfDays = 0
    cursor = 1

    while (cursor < month):
        totalOfDays += calendar.monthrange(year, cursor)[1]
        cursor += 1
    
    totalOfDays += day

    return totalOfDays 

def getPercentOfYearElapsed(daysElapsed):

    daysOfYear = 365 
    percent = round(100 * daysElapsed / daysOfYear, 1)
    return (percent)

def getYearsProgressPercent():

    dates = getDates()
    numberOfDaysElapsed = getNumberOfDaysElapsed(dates['currentDay'], dates['currentMonth'],dates['currentYear'])
    percent = getPercentOfYearElapsed(numberOfDaysElapsed)

    return (percent)