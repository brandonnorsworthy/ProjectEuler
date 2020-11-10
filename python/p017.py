#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

total = 0
count = 0

def main():
    global total
    global count
    for x in range(1001):
        numStr = ''
        #numStr = str(x)
        if x / 1000 >= 1:
            countStringAddToTotal(printThousands(x))
            continue
        if x / 100 >= 1:
            xOnes = x % 10
            xTens = x % 100
            numStr += printOnes(int(x/100))
            numStr += 'hundred'
            if x % 100 > 0:
                numStr += 'and'
            if x % 100 > 20:
                numStr += printTens((x - xOnes) % 100)
                numStr += printOnes(xOnes)
                countStringAddToTotal(numStr)
            else:
                if x % 100 < 10:
                    numStr += printOnes(xOnes)
                else:
                    numStr += printTens(xTens)
                countStringAddToTotal(numStr)
            continue
        if x / 10 >= 1:
            if x > 20:
                xOnes = x % 10
                numStr += printTens(x - xOnes)
                numStr += printOnes(xOnes)
                countStringAddToTotal(numStr)
            else:
                countStringAddToTotal(printTens(x))
            continue
        if x / 1 >= 1:
            countStringAddToTotal(printOnes(x))
            continue
    print(total, 'c', count)

def printOnes(number):
    numStr = ''
    if number == 1:
        numStr = 'one'
    elif number == 2:
        numStr = 'two'
    elif number == 3:
        numStr = 'three'
    elif number == 4:
        numStr = 'four'
    elif number == 5:
        numStr = 'five'
    elif number == 6:
        numStr = 'six'
    elif number == 7:
        numStr = 'seven'
    elif number == 8:
        numStr = 'eight'
    elif number == 9:
        numStr = 'nine'
    elif number == 0:
        numStr = ''
    return numStr

def printTens(number):
    numStr = ''
    if 10 <= number and number < 20:
        if number == 10:
            numStr = 'ten'
        elif number == 11:
            numStr = 'eleven'
        elif number == 12:
            numStr = 'twelve'
        elif number == 13:
            numStr = 'thirteen'
        elif number == 14:
            numStr = 'fourteen'
        elif number == 15:
            numStr = 'fifteen'
        elif number == 16:
            numStr = 'sixteen'
        elif number == 17:
            numStr = 'seventeen'
        elif number == 18:
            numStr = 'eighteen'
        elif number == 19:
            numStr = 'nineteen'
    elif 20 <= number and number < 30:
        numStr = 'twenty'
    elif 30 <= number and number < 40:
        numStr = 'thirty'
    elif 40 <= number and number < 50:
        numStr = 'forty'
    elif 50 <= number and number < 60:
        numStr = 'fifthy'
    elif 60 <= number and number < 70:
        numStr = 'sixty'
    elif 70 <= number and number < 80:
        numStr = 'seventy'
    elif 80 <= number and number < 90:
        numStr = 'eighty'
    elif 90 <= number and number < 100:
        numStr = 'ninty'
    elif number == 0:
        numStr = ''
    return numStr

def printHundreds(number):
    numStr = ''
    return numStr

def printThousands(number):
    numStr = 'onethousand'
    return numStr

def countStringAddToTotal(numStr):
    global count
    global total
    count += 1
    print(numStr)
    total += len(numStr)

if __name__ == "__main__":
    main()