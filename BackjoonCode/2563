#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;



int main()
{
	static int array[100][100];
	int N, x, y, Area;
	cin >> N;
	Area = 0;

	/*
//Place_dohwaji(array);
	for (int i = 0; i < 100; i++)
	{
		for (int j = 0; j < 100; j++)
		{
			array[i][j] = 0;
		}
	}
*/

	for (int i = 0; i < N; i++)
	{
		cin >> x >> y;
		for (int j = x; (j < x + 10 && j < 100); j++)
		{
			for (int k = y; (k < y + 10 && k < 100); k++)
			{
				array[j][k] = 1;
			}
		}
	}




	/*
	//Print_dohwaji(array);
	for (int i = 0; i < 100; i++)
	{
		for (int j = 0; j < 100; j++)
		{
			cout << array[i][j];
		}
		cout << endl;
	}
	*/

	for (int i = 0; i < 100; i++)
	{
		for (int j = 0; j < 100; j++)
		{
			if (array[i][j] == 1)
				Area ++;
		}

	}
	cout << Area;


	return 0;
}
















/*

int main()
{
	cin.tie(NULL);
	std::ios_base::sync_with_stdio(false);

	int N, M, count;
	cin >> N >> M;

	vector <int> num1(N);

	for (int i = 0; i < N; i++)
	{
		cin >> num1[i];
	}

	vector<pair<int, int>> range(M);
	//pair 선언

	for (int i = 0; i < M; i++)
	{
		cin >> range[i].first >> range[i].second;
		count = 0;
		for (int j = 0; j < N + 1; j++)
		{
			if (j >= (range[i].first) && j <= (range[i].second))
			{
				count = count + num1[j - 1];
			}
		}
		cout << count;
		if (i < M - 1)
			cout << endl;
	}

}
*/
