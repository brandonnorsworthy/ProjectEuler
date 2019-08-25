/*
Solution to Project Euler
Problem 1
Copyright Brandon Norsworthy 2019. All rights reserved.

https://github.com/brandonnorsworthy/ProjectEuler
https://projecteuler.net/archives
*/

#include <iostream>

int problem1()
{
	//initalize variables
	int limitNumber;
	int firstMultiple = 5;
	int secondMultiple = 3;
	int sumOfMultiples = 0;

	//prompt user for the max number
	std::cout << "Enter the maximum number: ";
	std::cin >> limitNumber;
	std::cout << std::endl;

	//take the multiples and divide them to see if they are greater or lower than the max number if they are lower then raise the value by 1 to make it higher than the max
	int maxFirstMultiple = (round(limitNumber / firstMultiple) * firstMultiple >= limitNumber ? limitNumber / firstMultiple : limitNumber / firstMultiple + 1);
	int maxSecondMultiple = (round(limitNumber / secondMultiple) * secondMultiple >= limitNumber ? limitNumber / secondMultiple : limitNumber / secondMultiple + 1);

	//multiply the number each time and then compare it by the max it can be and if its at the max then move on
	for (int i = 0; i < maxFirstMultiple; i++)
	{
		sumOfMultiples += firstMultiple * i;
	}

	//multiply the number each time and compare it to the max it can be and if its a multiple of the both the first and second then disregaurd because the loop above already  added it to the sum
	for (int i = 0; i < maxSecondMultiple; i++)
	{
		if ((secondMultiple * i) % firstMultiple == 0) {
			continue;
		}
		sumOfMultiples += secondMultiple * i;
	}

	//print out the sum for visibility
	std::cout << std::endl << "Sum: " << sumOfMultiples << std::endl;

	return 0;
}