#include <iostream>
using namespace std;
void main()
{
	int num;
	cin >> num;
	for (int i = 1; i < num+1; i++)
	{
		if (num % i == 0)
		{
			cout << i << endl;
		}

		if (i == num)
		{
			break;
		}
	}
}
