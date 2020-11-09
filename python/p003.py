#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def main():
    number = 55
    count = 2

    while True:
        if number % count == 0:
            if isPrimeNumber(count):
                break
        count += 1
        if count >= number:
            break
        continue

    print(number)

def testPrime(factor):
    for i in range(2, factor - 1):
        print(factor, '%', i, '==', factor % i == 0)
        if factor % i == 0:
            return False
    print('true')
    return True

def isPrimeNumber(number):
    for iterator in range(number - 1, 2):
        if number % iterator == 0:
            return True
        continue
    return False


if __name__ == "__main__":
    main()