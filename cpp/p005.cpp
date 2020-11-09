// Problem5.cpp : Defines the entry point for the console application.
/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

//#include "pch.h"
#include <iostream>

//methods
int problem5();
int divisibleCalculationsNoCout();
int divisibleCalculationsCout();
bool isDivisibleByAllNoCout();
bool isDivisibleByAllCout();
bool isDivisibleReset();

//input by user
int maxDivisible = 0;
char coutDisabledChar = 'f';
bool coutDisabled = true;

//variables preset
bool isDivisible[100];

int problem5()
{
	//variable that stores our number for what is divisible by everything used at end
	int num = 0;

	//ask user nicely for what they want <3
	std::cout << "Please enter the max number to be divisible by [max 20]: ";
	std::cin >> maxDivisible;
	std::cout << "Do you want cout on or off [t/f]: ";
	std::cin >> coutDisabledChar;

	if (coutDisabledChar == 't')
	{
		coutDisabled = true;
	}
	else
	{
		coutDisabled = false;
	}

	std::cout << "--------------------------------------------------" << std::endl;
	//reassure user its not broke
	if (!coutDisabled)
	{
		std::cout << "doing math magic";
		num = divisibleCalculationsNoCout();
	}
	else
	{
		num = divisibleCalculationsCout();
	}

	std::cout << std::endl << "--------------------------------------------------" << std::endl;
	std::cout << num << " is the lowest number divisible by 1 to " << maxDivisible << "." << std::endl;

	return 0;
}

//these are split to not have to do pointless calculations for the if statements for cout
int divisibleCalculationsNoCout()
{
	//calculations are done here
	for (int i = maxDivisible; i < 2400000000; i++)
	{
		isDivisibleReset();
		for (int j = 1; j < maxDivisible + 1; j++)
		{
			if (i % j == 0)
			{
				isDivisible[j - 1] = true;
			}
			else
			{
				break;
			}
		}
		if (isDivisibleByAllNoCout())
		{
			return i;
			break;
		}
	}

	return 0;
}

int divisibleCalculationsCout()
{
	//calculations are done here
	for (int i = maxDivisible; i < 2400000000; i++)
	{
		isDivisibleReset();
		for (int j = 1; j < maxDivisible + 1; j++)
		{
			if (i % j == 0)
			{
				isDivisible[j - 1] = true;
				std::cout << std::endl << "i = " << i << ", j = " << j << ", isDivisible[" << j - 1 << "] = " << isDivisible[j - 1];
			}
			else
			{
				std::cout << std::endl << "i = " << i << ", j = " << j << ", isDivisible[" << j - 1 << "] = " << isDivisible[j - 1];
				break;
			}
		}
		if (isDivisibleByAllCout())
		{
			return i;
			break;
		}
	}

	return 0;
}

//checks if all array elements are set to true meaning it was divisible by all factors 1 to maxDivisible
bool isDivisibleByAllNoCout()
{
	if (isDivisible[0] == true)
	{
		for (int i = 0; i < maxDivisible; i++)
		{
			if (isDivisible[i] == true)
			{
				continue;
			}
			else
			{
				return false;
			}
		}
		return true;
	}
	return false;
}

bool isDivisibleByAllCout()
{
	if (isDivisible[0] == true)
	{
		for (int i = 0; i < maxDivisible; i++)
		{
			if (isDivisible[i] == true)
			{
				continue;
			}
			else
			{
				std::cout << ", # isDivisibleByAll()";
				return false;
			}
		}
		std::cout << ", % isDivisibleByAll true";
		return true;
	}
	std::cout << ", @ nothing happened";

	return false;
}

//reset the isDivisible[] to all false for another run bois
bool isDivisibleReset()
{
	for (int i = 0; i < maxDivisible; i++)
	{
		isDivisible[i] = false;
	}

	return false;
}