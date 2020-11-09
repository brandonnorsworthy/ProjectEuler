#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#1^2 + 2^2 = x
#(1 + 2) ^2=y
#x - y = z

x = 0
y = 0
for ix in range(1,101):
    x += ix * ix

for iy in range(1,101):
    y += iy
y *= y

print(y - x)