/*
gaolex
2017-03-18
1007
*/

#include <iostream>
using namespace std;
int main()
{
    int k;
    float sum = 0.0;
    cin >> k;
    float i = 1.0;
    for (;; i++)
    {
	sum += 1.0 / i;
	if (sum > k)
	    break;
    }
    cout << i << endl;
	
    return 0;
}