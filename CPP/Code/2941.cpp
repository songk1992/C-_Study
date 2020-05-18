#include <iostream> 
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string x_1;
int cnt=0;

int main()
{
	cin.tie(NULL);
	std::ios_base::sync_with_stdio(false);
	cin >> x_1;

	//cout << "1 " << x_1 << " length " <<x_1.length()<< endl;
	for (int i = 0; i < x_1.length() - 2; i++)
	{
		
	}
	//cout << "1 " << x_1 << " cnt " << cnt << endl;
	for (int i = 0; i < (x_1.length())-1; i++)
	{
		if (i < (x_1.length()) - 2)
		{
			if (x_1[i] == 'd' && x_1[i + 1] == 'z' && x_1[i + 2] == '=')
			{
				x_1[i] = '0';
				x_1[i + 1] = '0';
				x_1[i + 2] = '0';
				cnt++;
			}
		}
	
		if (x_1[i] == 'c' && x_1[i + 1] == '=')
		{
			x_1[i] = '0';
			x_1[i + 1] = '0';
			cnt++;
		}

		if (x_1[i] == 'c' && x_1[i + 1] == '-')
		{
			x_1[i] = '0';
			x_1[i + 1] = '0';
			cnt++;
		}

		if (x_1[i] == 'd' && x_1[i + 1] == '-')
		{
			x_1[i] = '0';
			x_1[i + 1] = '0';
			cnt++;
		}

		if (x_1[i] == 'l' && x_1[i + 1] == 'j')
		{
			x_1[i] = '0';
			x_1[i + 1] = '0';
			cnt++;
		}

		if (x_1[i] == 'n' && x_1[i + 1] == 'j')
		{
			x_1[i] = '0';
			x_1[i + 1] = '0';
			cnt++;
		}
		if (x_1[i] == 's' && x_1[i + 1] == '=')
		{
			x_1[i] = '0';
			x_1[i + 1] = '0';
			cnt++;
		}
		if (x_1[i] == 'z' && x_1[i + 1] == '=')
		{
			x_1[i] = '0';
			x_1[i + 1] = '0';
			cnt++;
		}
	}
	//cout << "2 " << x_1 << " cnt " << cnt << endl;
	for (int i = 0; i < (x_1.length()); i++)
	{
		if (x_1[i] != '0')
		{
			cnt++;
		}
	}
	//cout << "3 " << x_1 << " cnt " << cnt << endl;
	cout << cnt;
}
