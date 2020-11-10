#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million.

longestChain = 0
longestChainNumber = 0

for x in range(2, 1000000):
    chainLength = 0
    tempNum = x
    while tempNum != 1:
        if tempNum % 2 == 0:
            tempNum = tempNum / 2
            chainLength += 1
        else:
            tempNum = 3 * tempNum + 1
            chainLength += 1
    chainLength += 1
    if chainLength > longestChain:
        longestChain = chainLength
        longestChainNumber = x
    continue

print(longestChainNumber)