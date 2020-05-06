#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
	ios::sync_with_stdio;
	cin.tie(0);
	// 속도 빠르게함
	
	int N;
	cin >> N;
	vector<pair<int, int>> num(N);
	//pair 선언

	for (int i = 0; i < N; i++)
	{
		cin >> num[i].first >> num[i].second;
	}
	for (int i = 0; i < N; i++)
	{
		cout<< num[i].first << num[i].second<<"\n";
	}

}
