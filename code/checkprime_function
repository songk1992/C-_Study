#include <iostream>
using namespace std;

int CP(int);
//Check Prime

int main()
{
	int n;

	cout << "Enter a positive integer:";

		cin >> n;

		if (CP(n) == 0)
			cout << n << "is prime";
		else
			cout << n << "is not prime";

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


