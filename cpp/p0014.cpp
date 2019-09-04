/*
Solution to Project Euler
Problem 14
Copyright Brandon Norsworthy 2019. All rights reserved.

https://github.com/brandonnorsworthy/ProjectEuler
https://projecteuler.net/archives
*/

#include <iostream>

int collatzSequence(int);

int main() {
	int largestChain = 0;
	int largestChainNumber = 0;

	int temp = 0;

	for (int i = 2; i < 1000000; i++)
	{
		int tempChain = collatzSequence(i);

		if (tempChain > largestChain)
		{
			largestChain = tempChain;
			largestChainNumber = i;
		}
	}

	std::cout << largestChainNumber;
}

int collatzSequence(int input) {
	long long int value = input;
	int chainValue = 0;

	while (value != 1) {
		chainValue += 1;
		if (value % 2 == 0)
		{
			//even
			value = value / 2;
		}
		else
		{
			//odd
			value = 3 * value + 1;
		}
	}
	return chainValue;
}