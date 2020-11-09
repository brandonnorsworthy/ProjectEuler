#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

found = False
for x in reversed(range(900,1000)):
    for y in reversed(range(900,1000)):
        number = x * y
        print(str(number)[0:3], ' r', str(number)[6:2:-1], ' x', x, ' y', y)
        found = True
        break

    if found:
        break