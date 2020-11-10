#You are given the following information, but you may prefer to do some research for yourself.
#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

dayOfTheWeek = 'monday'
dayOfTheMonth = 1
daysInTheMonth = 31
monthCurrent = 'january'
monthOfTheYear = 1
yearCurrent = 1900
yearToDate = 0

def main():
    global dayOfTheWeek
    global dayOfTheMonth
    global daysInTheMonth
    global monthCurrent
    global monthOfTheYear
    global yearCurrent
    global yearToDate

    total = 0

    while True:
        advanceDayOfTheMonth()
        if dayOfTheMonth > daysInTheMonth:
            advanceMonth()
        if monthOfTheYear > 12:
            advanceYear()
        if yearCurrent > 1900:
            if dayOfTheWeek == 'sunday' and dayOfTheMonth == 1:
                #print(dayOfTheWeek, ',', monthCurrent, dayOfTheMonth, ',', yearCurrent)
                total += 1
        if yearCurrent > 2000:
            break
    print(dayOfTheWeek, ',', monthCurrent, dayOfTheMonth, ',', yearCurrent)
    print(total)

def advanceDayOfTheMonth():
    global dayOfTheMonth
    dayOfTheMonth += 1
    setDayOfTheWeek()

def advanceMonth():
    global monthOfTheYear
    global dayOfTheMonth
    monthOfTheYear += 1
    dayOfTheMonth = 1
    setMonth()
    getMonthDays()

def advanceYear():
    global yearCurrent
    global yearToDate
    global monthOfTheYear
    yearCurrent += 1
    yearToDate += 1
    monthOfTheYear = 1
    setMonth()

def getMonthDays():
    global yearToDate
    global monthOfTheYear
    if monthOfTheYear == 4 or monthOfTheYear == 6 or monthOfTheYear == 9 or monthOfTheYear == 11:
        return 30
    elif monthOfTheYear == 2:
        if yearToDate % 4 == 0:
            return 29
        else:
            return 28
    else:
        return 31

def setDayOfTheWeek():
    global dayOfTheWeek
    if dayOfTheWeek == 'monday':
        dayOfTheWeek = 'tuesday'
    elif dayOfTheWeek == 'tuesday':
        dayOfTheWeek = 'wednesday'
    elif dayOfTheWeek == 'wednesday':
        dayOfTheWeek = 'thursday'
    elif dayOfTheWeek == 'thursday':
        dayOfTheWeek = 'friday'
    elif dayOfTheWeek == 'friday':
        dayOfTheWeek = 'saturday'
    elif dayOfTheWeek == 'saturday':
        dayOfTheWeek = 'sunday'
    elif dayOfTheWeek == 'sunday':
        dayOfTheWeek = 'monday'
    else:
        dayOfTheWeek = 'error'

def setMonth():
    global monthCurrent
    global monthOfTheYear
    if monthOfTheYear == 1:
        monthCurrent = 'january'
    elif monthOfTheYear == 2:
        monthCurrent = 'february'
    elif monthOfTheYear == 3:
        monthCurrent = 'march'
    elif monthOfTheYear == 4:
        monthCurrent = 'april'
    elif monthOfTheYear == 5:
        monthCurrent = 'may'
    elif monthOfTheYear == 6:
        monthCurrent = 'june'
    elif monthOfTheYear == 7:
        monthCurrent = 'july'
    elif monthOfTheYear == 8:
        monthCurrent = 'august'
    elif monthOfTheYear == 9:
        monthCurrent = 'september'
    elif monthOfTheYear == 10:
        monthCurrent = 'october'
    elif monthOfTheYear == 11:
        monthCurrent = 'november'
    elif monthOfTheYear == 12:
        monthCurrent = 'december'
    else:
        monthCurrent = 'error'

if __name__ == "__main__":
    main()