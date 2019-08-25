/*
Solution to Project Euler
Problem 2
Copyright Brandon Norsworthy 2019. All rights reserved.

https://github.com/brandonnorsworthy/ProjectEuler
https://projecteuler.net/archives
*/

#include <iostream>

//given starting numbers
int a = 1;
int b = 2;

int main()
{
	//example wants even-valued terms in sum only
	//start at 2 because the second term is even
	int sum = 2;

	while (a + b < 4000000) {
		int tempB = b;
		b = a + b;
		a = tempB;
		//do modulous division to make sure we are only grabbing the even values
		if (b % 2 == 0)
		{
			sum += b;
		}
	}

	std::cout << sum << std::endl;

	return 0;
}