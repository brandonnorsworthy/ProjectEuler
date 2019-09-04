/*
Solution to Project Euler
Problem 12
Copyright Brandon Norsworthy 2019. All rights reserved.

https://github.com/brandonnorsworthy/ProjectEuler
https://projecteuler.net/archives
*/

#include <iostream>

long long int findFactors(long long int);

long long int naturalNumber = 1;

int main() {
	//numbers start
	long long int triangularNumber = 0;
	//number of factors limit
	int factorLimit = 0;
	bool factorLimitReached = false;

	std::cout << "Number of divisor limit : ";
	std::cin >> factorLimit;

	while (factorLimitReached == false)
	{
		triangularNumber += naturalNumber;
		naturalNumber += 1;
		if (triangularNumber % 2 == 0 && triangularNumber > 76000000)
		{
			if (findFactors(triangularNumber) > factorLimit)
			{
				factorLimitReached = true;
			}
		}
	}

	std::cout << triangularNumber << " " << findFactors(triangularNumber);

	return 0;
}

long long int findFactors(long long int triangularNumber) {
	int factorAmount = 0;

	for (long long int i = 1; i <= triangularNumber; i++)
	{
		if (triangularNumber % i == 0)
		{
			factorAmount += 1;
		}
	}

	return factorAmount;
}