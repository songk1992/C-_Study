#include <iostream>
using namespace std;

int main()
{
	int C, K, P, Sum;
	cin >> C >> K >> P;
	Sum = 0;

	int i = 0;
	while (i<=C)
	{
		Sum = Sum + (K * i) + (P * pow(i,2));
		i++;
	}
	cout << Sum;
	return 0;
}
