#include <iostream>
using namespace std;
void main()
{
	int num;
	cin >> num;
	for (int i = 2; i < num; i++)
	{
		if (num % i == 0)
		{
			cout << num << "not prime number" << endl;
			break;
		}

			if (i == num)
			cout << num << "is prime number" << endl;
	}
}
