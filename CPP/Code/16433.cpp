#include<iostream>

using namespace std;

int N,R,C,flag;

void insert()
{
	cin >> N>>R>>C;
}
void calculate()
{
	flag = 0;
	if ((R + C) % 2 == 0)flag = 1;
}
void Print()
{
	for (int i = 0; i < N; i++)
	{
		for (int j = 1; j < N+1; j++)
		{
			if ((flag + i) % 2 == 1)
			{
				if (j % 2 == 1) { cout << "v"; }
				else if (j % 2 == 0) { cout << "."; }
			}
			else if ((flag + i) % 2 == 0)
			{
				if (j % 2 == 0) { cout << "v"; }
				else if (j % 2 == 1) { cout << "."; }
			}
		}
		cout << endl;

	}
}

int main()
{
	insert();
	calculate();
	Print();
}
