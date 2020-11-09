#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

count = 0
sum = 0

while True:
    count += 1
    if count >= 1000:
        break
    if count % 3 == 0 or count % 5 == 0:
        sum += count
    continue

print(sum)