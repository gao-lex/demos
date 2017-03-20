#include<iostream>
using namespace std;

int main()
{
	int s;
	cin >> s;
	int zhouchang=0;
	for (int kuan = 1; kuan < floor(sqrt(s)) || kuan == floor(sqrt(s)); kuan++)
	{
		int chang = s / kuan;
		if (kuan*chang == s)
			zhouchang = 2 * (kuan + chang);
	}
	cout << zhouchang << endl;
	return 0;
}