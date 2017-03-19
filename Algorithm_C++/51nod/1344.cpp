#include<iostream>
#include<vector>
#include<numeric>
using namespace std;

int main()
{
	int n;
	vector<int> box;
	vector<long long int> sum;
	while (cin >> n)
		box.push_back(n);
	long long int min = box[1];
	for (int i = 1; i < box.size(); i++)
	{
		long long int mintemp = i > 1 ? sum[i - 2] + box[i] : box[1];
		sum.push_back(mintemp);
		if (mintemp < min)
			min = mintemp;
	}
	if (min < 0)
		cout << 0 - min;
	else
		cout << 0;

}