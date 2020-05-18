#include <iostream>
using namespace std;

int main()
{
	int t,n,sum,GPA[1000];
	double average, count;

	cin >> t;

	for (int i = 0; i < t; i++)
	{
		sum = 0;
		count = 0;
		int GPA[1000] = { 0, };
		cin >> n;

		for (int j = 0; j < n; j++)
		{
			cin >> GPA[j];
			sum += GPA[j];
		}
		average = sum / n;
		
		for (int k = 0; k < n; k++)
		{
			if (average < GPA[k])
			{
				count++;
			}
		}

		cout << fixed;
		cout.precision(3);
		cout << (count/n) * 100<<'\%' << endl;
	}
}
