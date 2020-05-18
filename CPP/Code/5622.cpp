#include<iostream>
#include<string>

using namespace std;
int n = 0;

int main()
{
	string str;
	cin >> str;

	for (int i = 0; i < str.size(); i++)
	{
		if (str[i] == 'A' || str[i] == 'B' || str[i] == 'C')
		{
			n += 3;
		}
		else if (str[i] == 'D' || str[i] == 'E' || str[i] == 'F')
		{
			n += 4;
		}
		else if (str[i] == 'G' || str[i] == 'H' || str[i] == 'I')
		{
			n += 5;
		}
		else if (str[i] == 'J' || str[i] == 'K' || str[i] == 'L')
		{
			n += 6;
		}
		else if (str[i] == 'M' || str[i] == 'N' || str[i] == 'O')
		{
			n += 7;
		}
		else if (str[i] == 'P' || str[i] == 'Q' || str[i] == 'R' || str[i] == 'S')
		{
			n += 8;
		}
		else if (str[i] == 'T' || str[i] == 'U' || str[i] == 'V')
		{
			n += 9;
		}
		else if (str[i] == 'W' || str[i] == 'X' || str[i] == 'Y' || str[i] == 'Z')
		{
			n += 10;
		}
		else if (str[i] == '1')
		{
			n += 2;
		}
		else if (str[i] == '0')
		{
			n += 11;
		}
	}
	cout << n;
	return 0;
}
