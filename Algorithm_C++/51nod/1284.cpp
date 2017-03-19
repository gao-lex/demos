#include <stdio.h>
#include <string.h>
#include <stdlib.h> 
typedef long long ll;
int main()
{
	//sum=a-b-c-d   sum=n-sum
	ll a; //A1+A2+A3+A4
	ll b; //A1A2+A1A3+A1A4+A2A3+A2A4+A3A4
	ll c; //A1A2A3+A1A2A4+A1A3A4+A2A3A4
	ll d; //A1A2A3A4 
	ll n,sum;
	while(scanf("%lld",&n)!=EOF){
		a=n/2+n/3+n/5+n/7;
		b=n/6+n/10+n/14+n/15+n/21+n/35;
		c=n/30+n/42+n/70+n/105;
		d=n/210;
		sum=n-a+b-c+d;
		printf("%lld\n",sum);
	}
	return 0;
}