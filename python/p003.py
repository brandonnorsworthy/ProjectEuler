#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

number = 600851475143

for x in range(2, int(number/2)):
    if number % x != 0:
        continue
    oppositex = int(number / x)
    foundPrime = True
    for y in range(2, int(oppositex/2) - 1):
        if oppositex % y == 0:
            foundPrime = False
            break
    if(foundPrime == True):
        print(oppositex)
        break
    continue