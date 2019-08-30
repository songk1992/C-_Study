#include <iostream>
using namespace std;

int N, a[1000];
double compare, sum;

int main()
{

	cin >> N;
	compare = 0;

	for (int i = 0; i < N; i++)
	{
		cin >> a[i];
		if (compare < a[i])compare = a[i];
	}

	for (int i = 0; i < N; i++)
	{
		sum += (a[i]/compare)*100;
	}
	cout << sum / N;
}
