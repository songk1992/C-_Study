#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
	cin.tie(NULL);
	std::ios_base::sync_with_stdio(false);

	static int arr[9];
	int sum = 0;
	int temp;

	for (int i = 0; i < 9; i++)
	{
		cin >> arr[i];
		sum += arr[i];
	}
	for (int i = 0; i < 9; i++)
	{
		for (int j = 0; j < 9; j++)
		{

			if ((i != j) && (sum == (arr[j] + arr[i] + 100)))
			{
				arr[j] = 0;
				arr[i] = 0;

				sort(arr, arr + 9);
				sum = 0;
				for (int i1 = 2; i1 < 9; i1++)
				{
						cout << arr[i1];
						if (i1 < 8)
						{
							cout << endl;

						}

				}
				return 0;
			}
		}
	}
}

