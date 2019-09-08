#include <iostream>
using namespace std;

int main() 
{
	long long int N,sum,S,count;
	cin >> S;
	sum = 0;
	count = 0;

	if (S == 1)
	{
		cout << 1;
		return 0;
	}

	for (int i = 1; i < S+1; i++)
	{

		sum += i;
		if (sum > S)
		{
			cout << count;
			return 0;
		}
		count++;
	}

}
