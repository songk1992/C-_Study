#include <iostream>
#include <conio.h>
using namespace std;
#pragma warning(disable:4996)

int main()
{
	int n, min = 1, max = 99,point, input;

		char a = getch();
		cout << "*";
		char b = getch();
		cout << "*\n\n";
		n = (a - '0') * 10 + (b - '0');

		for (int i = 0; i < 10; i++)
		{
			cout << i << "회" << min << "부터" << max << "까지 예측";
			cin >> input;

			point = i;
			if (n == input)break;

			else if (n > input)
			{
				cout << "더 큰 숫자 입니다!";
			}

			else
			{
				cout << "더 작은 숫자 입니다!";
			}
		}

		cout << "정답은 " << n << (n == input) ? "성공" : "실패";
		cout << "최종점수" << 10 * (10 - point);

}
