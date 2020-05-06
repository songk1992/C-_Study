#include <iostream>
#include <algorithm>
using namespace std;


void Print(int* arr)
{
	cout << "arr[i] : ";
	for (int i = 0; i < 5; i++)
	{
		cout << arr[i] << " ";
	}
	cout << endl;
}

int main()
{
	int arr[5];
	for (int i = 0; i < 5; i++)
	{
		cin >> arr[i]; 
	}
	Print(arr);
	sort(arr, arr + 5);
	Print(arr);
	return 0;
}
	
