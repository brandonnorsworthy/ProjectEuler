#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

foundnumber = 0
for x in reversed(range(900,1000)):
    for y in reversed(range(900,1000)):
        number = x * y
        
        #print(str(number)[0:3], ' r', str(number)[6:2:-1], ' x', x, ' y', y)

        str1 = str(number)[0:3]
        str2 = str(number)[6:2:-1]

        if(str1 == str2):
            foundnumber = number
            break

    if foundnumber != 0:
        break

print(foundnumber)