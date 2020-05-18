#include <iostream>

using namespace std;

int n1,n2, o1,o2, a;


int main()
{

	cin >> n1 >> n2;

	o1 = n1 / 100 + n1 / 10 % 10 * 10 + n1 % 10 * 100;
	o2 = n2 / 100 + n2 / 10 % 10 * 10 + n2 % 10 * 100;

	(o1 > o2 ? a = o1 : a = o2);

	cout << a;
}
