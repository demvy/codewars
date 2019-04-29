#include <iostream>
#include <map>
#include <vector>

/*
Enough is enough!
Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, and now they want to show Charlie their entire collection. However, Charlie doesn't like this sessions, since the motive usually repeats. He isn't fond of seeing the Eiffel tower 40 times. He tells them that he will only sit during the session if they show the same motive at most N times. Luckily, Alice and Bob are able to encode the motive as a number. Can you help them to remove numbers such that their list contains each number only up to N times, without changing the order?

Task
Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

Example
  delete_nth ([1,1,1,1],2) # return [1,1]

  delete_nth ([20,37,20,21],1) # return [20,37,21]

*/

std::vector<int> deleteNth(std::vector<int> arr, int n)
{
	std::map<int, int> counter;
	std::map<int, int>::iterator map_it = counter.begin();
	std::vector<int>::iterator it = arr.begin();

	while (it != arr.end())
	{
		map_it = counter.find(*it);
		if (map_it != counter.end())
		{
			map_it->second += 1;
			if (map_it->second > n)
				it = arr.erase(it);
			else
				it++;
		}
		else  // not found in map as counter																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																													
		{
			counter[*it] = 1;
			it++;
		}
	}
	counter.empty();
	return arr;
}

int main(void)
{
	std::vector<int> a = {1,1,3,3,7,2,2,2,2};
	std::vector<int> res;

	res = deleteNth(a, 3);
	for(auto i = res.begin(); i < res.end(); i++)
	{
		std::cout << *i << " " << std::flush;
	}
	return 0;
}