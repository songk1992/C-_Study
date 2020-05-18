

#include<iostream>

using namespace std;

int SCM,a, b,GCD,big,temp,T;
int a1[1000];
int b1[1000];


int main()
{
	

	cin >> T;
	

	for (int k = 0; k < T; k++)
	{
		GCD = 1;
		int a1[1000] = { 0, };
		int b1[1000] = { 0, };

		cin >> a >> b;
		if (a > b)
		{
			big = a;
		}
		if (a < b)
		{
			big = b;
		}

		for (int i = 1; i < big; i++)
		{
			if (a % i == 0)
				a1[i] = i;
			//a의 약수 집합

			if (b % i == 0)
				b1[i] = i;
			//b의 약수 집합
		}

		for (int i = 1; i < big; i++)
		{
			for (int j = 1; j < big; j++)
			{
				if (a1[i] == b1[j])
				{
					if (GCD <= a1[i])
					{
						GCD = a1[i];
					}
				}
			}
		}


		SCM = (a / GCD) * b;

		cout << SCM << " " << GCD;

		if (T > 1+k)cout << endl;

	}
}
