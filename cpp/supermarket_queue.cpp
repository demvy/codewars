/*
There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

The function has two input variables:

customers: an array (list in python) of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
The function should return an integer, the total time required.

EDIT: A lot of people have been confused in the comments. To try to prevent any more confusion:

There is only ONE queue, and
The order of the queue NEVER changes, and
Assume that the front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.
The diagram on the wiki page I linked to at the bottom of the description may be useful.
So, for example:

queueTime(std::vector<int>{5,3,4}, 1)
// should return 12
// because when n=1, the total time is just the sum of the times

queueTime(std::vector<int>{10,2,3,3}, 2)
// should return 10
// because here n=2 and the 2nd, 3rd, and 4th people in the 
// queue finish before the 1st person has finished.

queueTime(std::vector<int>{2,3,10}, 2)
// should return 12
N.B. You should assume that all the test input will be valid, as specified above.

P.S. The situation in this kata can be likened to the more-computer-science-related idea of a thread pool, with relation to running multiple processes at the same time: https://en.wikipedia.org/wiki/Thread_pool
*/

#include <iostream>
#include <vector>
#include <algorithm>

long queueTime(std::vector<int> customers,int n){
	if (customers.size() && n > 0) {
		std::vector<int> tills(customers.begin(), (customers.begin() + n < customers.end()) ? customers.begin() + n : customers.end());
		long res = 0;
		int min = 0;
		auto it = customers.begin() + n;

		while (it < customers.end()) {
			min = *(std::min_element(tills.begin(), tills.end()));
			res += min;
			for (auto el = tills.begin(); el < tills.end(); el++) {
				*el -= min;
				if (*el <= 0) {
					*el = (it < customers.end()) ? *it++: 0;
				}
			}
		}

		return res + *(std::max_element(tills.begin(), tills.end()));
	}
	return 0;
}

int main(void) {
	std::cout << queueTime(std::vector<int>{4,2,6,8,178,14,3,7,8,11,56}, 3) << std::endl;
	std::cout << queueTime(std::vector<int>{1,1,1,1}, 3) << std::endl;
	std::cout << queueTime(std::vector<int>{6,3,1,7,5,4}, 2) << std::endl;
}