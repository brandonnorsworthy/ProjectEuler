#The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#We can see that 28 is the first triangle number to have over five divisors.
#What is the value of the first triangle number to have over five hundred divisors?

import math

number = 0
count = 0
while True:
    triangleNumber = 0
    factorNumber = 0
    for x in range(count + 1):
        triangleNumber += x
    for y in range(1, int(math.isqrt(triangleNumber) + 1)):
        if triangleNumber % y == 0:
            #print('count', count, 'triangle number', triangleNumber, 'number of factors', factorNumber, 'divisor', y)
            if triangleNumber / y == y:
                factorNumber += 1
            else:
                factorNumber += 2
    if factorNumber > 500:
        number = triangleNumber
        break
    count += 1
    continue

print(number)