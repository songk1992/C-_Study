#include <iostream>
using namespace std;

int main()
{
	int N, A;
	cin >> N;

	A = N;
	for (int i = 0; i < N; i++)
	{
		for (int j =N-i; j > 1; j--)
		{
			cout << " ";
		}
		
		for (int j = 0; j < 2*i+1; j++)
		{
			cout << "*";
		}

		cout<<endl;
	}
	--N;
	A = N;
	for (int i = 0; i < N; i++)
	{

		for (int j = 0; j < i+1; j++)
		{
			cout << ' ';
		}

		for (int j = 0; j < ((2 * A) - 1); j++)
		{
			cout << '*';
		}


		A--;
		if (A < 1)  return 0;
		cout << endl;
	}

	return 0;

}
