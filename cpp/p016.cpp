/*
Solution to Project Euler
Problem 16
Copyright Brandon Norsworthy 2019. All rights reserved.

https://github.com/brandonnorsworthy/ProjectEuler
https://projecteuler.net/archives
*/

#include <iostream>


int main() {
	int power = 1000;
	long long int product = 1;
	long long int digitSum = 0;

	for (int i = 1; i <= power; i++)
	{
		product *= 2;
	}

	std::cout << product << std::endl;
	int numberofDigits = 0;

	do {
		++numberofDigits;
		product /= 10;
	} while (product);

	std::cout << numberofDigits;
}