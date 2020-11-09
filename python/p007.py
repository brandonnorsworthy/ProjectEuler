#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

count = 3
number = 0
x = 6
while True:
    isPrime = True
    for y in range(2, int(x/2)):
        if x % y == 0:
            isPrime = False
            break
        continue
    if isPrime:
        count += 1
    if count >= 10001:
        number = x
        break
    x += 1
    continue

print(number)