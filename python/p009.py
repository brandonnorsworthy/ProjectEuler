#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

import math

stop = False
product = 0
for a in range(400):
    total = 0
    for b in range(500):
        squared = a*a + b*b
        if squared == math.isqrt(squared) ** 2:
            total = int(math.sqrt(squared)) + a + b
        if total == 1000:
           product = a * b * math.isqrt(squared)
           stop = True
           break
    if stop == True:
        break

print(product)