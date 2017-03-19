#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	int n,temp;
	int sum=0;
	vector<int> a;
	cin >> n;
	while (cin>>n)
		a.push_back(n);
	int num1 = count(a.begin(),a.end(),1);
	int num2 = count(a.begin(), a.end(), 2);
	int other = a.size() - num1 - num2;
	cout << num1*(num1 + num2 + other - 1) + num2*(num2 - 1) / 2;
	return 0;
}