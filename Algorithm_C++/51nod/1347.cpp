#include<iostream>
#include<string>
using namespace std;
bool duichuan(string & cs) {
	if (cs.length() % 2 == 0 && (cs.substr(cs.length() / 2) == cs.substr(0, cs.length() / 2)))
	{
		return true;
	}
	else
		return false;
}

int main()
{
	string s;
	cin >> s;
	if (duichuan(s)) { cout << "YES" << endl; }
	else cout << "NO";
	return 0;
}