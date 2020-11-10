#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

import math

number = 10

isPrime = True
for i in range(6, 2000001):
    isPrime = True
    for x in range(2, int(math.sqrt(i) + 1)):
        if i % x == 0:
            isPrime = False
            break
    if isPrime:
        number += i
    continue

print(number)