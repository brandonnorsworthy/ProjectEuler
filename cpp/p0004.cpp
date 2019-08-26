/*
Solution to Project Euler
Problem 4
Copyright Brandon Norsworthy 2019. All rights reserved.

https://github.com/brandonnorsworthy/ProjectEuler
https://projecteuler.net/archives
*/

#include <string>
#include <iostream>

bool isPalindrome(int);

int main()
{
	int largestPalindrome = 0;

	for (int i = 999; i > 900; i--)
	{
		for (int j = 999; j > 900; j--)
		{
			int num = i * j;
			if (isPalindrome(num))
			{
				if (num > largestPalindrome)
				{
					largestPalindrome = num;
				}
			}
		}
	}

	std::cout << largestPalindrome << std::endl;

	return 0;
}

bool isPalindrome(int num)
{
	std::string str = std::to_string(num);

	if (str == std::string(str.rbegin(), str.rend())) {
		return true;
	}

	return false;
}
