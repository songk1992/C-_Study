#include <iostream>
using namespace std;

int CP(int);
//Check Prime

int main()
{
	int t, n, count=0;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> n;

		if ((CP(n) == 0)&&(n!=1))
		{
			count++;
		}
		else
		{
			continue;
		}
	}

	cout << count;
	return 0;

}


int CP(int n)
{
	bool flag = false;
	
	for (int i = 2; i <= n/2; ++i)
	{
		if (n % i == 0)
		{
			flag = true;
			break;
		}
	}
	return flag;
}


