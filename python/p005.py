#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

number = 0
count = 1
while True:
    currentTest = True
    for i in range(1,20):
        if count % i != 0:
            currentTest = False
            break
    if currentTest == True:
        number = count
        break
    count += 1
    continue

print(number)