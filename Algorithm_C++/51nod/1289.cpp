#include<iostream>
#include<vector>
#include<algorithm>
#include<stack>
using namespace std;

int main()
{
	int n; 
	cin >> n;
	int fish,dir;
	stack<int> fishes;
	while (cin >> fish >> dir) {
		if (dir == 1)
			fishes.push(fish);
		else
		{
			while (fishes.size() != 0)
			{
				if (fish > fishes.top())
				{
					fishes.pop();
					n--;
				}
				else {
					n--;
					break;
				}
			}
		}
	}
	cout << n;
	return 0;
}