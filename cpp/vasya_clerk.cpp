/*
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?

Return YES, if Vasya can sell a ticket to each person and give the change with the bills he has at hand at that moment. Otherwise return NO.

Examples:
tickets({25, 25, 50}) // => YES 
tickets({25, 100}) // => NO. Vasya will not have enough money to give change to 100 dollars
tickets({25, 25, 50, 50, 100}) // => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>

std::string tickets(const std::vector<int> peopleInLine){
	if (peopleInLine.size())
	{
		std::vector<int> cash_box = {};
		std::map<int, std::vector<std::vector<int>>> change_map = {{25, {{0}}}, {50, {{25}}}, {100, {{25, 50}, {25, 25, 25}}}};
		std::vector<int>::iterator where;
		std::vector<std::vector<int>>::iterator j;

		for(auto it = peopleInLine.begin(); it < peopleInLine.end(); it++)
		{
			if (*it == 50 || *it == 100)
			{
				// Check if we have change for people's cache
				int res; // result of check all vectors for money value
				
				for(j = change_map[*it].begin(); j < change_map[*it].end(); j++)
				{
					res = 1;

					for (auto k = (*j).begin(); k < (*j).end(); k++)
					{
						where = find(cash_box.begin(), cash_box.end(), *k);
						if (where == cash_box.end())
							res = 0;
					}
					if (res)
						break;
				}
				if (res)
				{
					for (auto k = (*j).begin(); k < (*j).end(); k++)
					{
						where = find(cash_box.begin(), cash_box.end(), *k);
						if (where != cash_box.end())
							// Delete change fron cash box if we have it
							cash_box.erase(where);
						else
							return "NO";
					}
					// If we have all change, add people's money to cash box
					cash_box.push_back(*it);
				}
				else
					return "NO";
			}
			else
				cash_box.push_back(*it);
		}
	}
	return "YES";
}

int main(void)
{
	//Should return YES, 25*3 can be change for 100
	std::vector<int> a = {25,100};

	std::cout << tickets(a) << std::endl;
	return 0;
}