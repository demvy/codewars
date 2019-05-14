/*
A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits):

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1634 (4 digits):

    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
The Challenge:

Your code must return true or false depending upon whether the given number is a Narcissistic number in base 10.

Error checking for text strings or other invalid inputs is not required, only valid integers will be passed into the function.

	It(test1)
	{
		Assert::That(narcissistic(7), Equals(true));
	}
	It(test2)
	{
		Assert::That(narcissistic(371), Equals(true));
	}
  It(test3)
	{
		Assert::That(narcissistic(122), Equals(false));
	}
  It(test4)
	{
		Assert::That(narcissistic(4887), Equals(false));
*/

#include <iostream>
#include <string>
#include <math.h>


bool narcissistic( int value ) {
	int res = 0;
	int len = std::to_string(value).length();
	int cmp = value;

	while (value) {
		res += (int)(pow(value % 10, len));
		value /= 10;
	}
	return cmp == res;
}

int main(void)
{
	std::cout << narcissistic(7) << std::endl;
	std::cout << narcissistic(371) << std::endl;
	std::cout << narcissistic(122) << std::endl;
	std::cout << narcissistic(4887) << std::endl;

	return 0;
}