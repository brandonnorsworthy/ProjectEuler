/*
Solution to Project Euler
Problem 1
Copyright Brandon Norsworthy 2019. All rights reserved.

https://github.com/brandonnorsworthy/ProjectEuler
https://projecteuler.net/archives
*/

#include <iostream>

bool isFactorPrime(long long int);

int main()
{
	//number to find largest prime from
	long long int number;
	bool factorFound = false;

	std::cout << "Enter the max number to find a prime from: ";
	std::cin >> number;

	for (int i = 2; i < number / 2; i++)
	{
		if (number % i == 0) {
			long long int j = number / i;
			if (isFactorPrime(j)) {
				std::cout << "Prime factor found " << j << std::endl;
			}
		}
	}

	return 0;
}

bool isFactorPrime(long long int input)
{
	for (int i = input / 2; i > 2; i--)
	{
		if (input % i == 0)
		{
			return false;
		}
	}

	return true;
}