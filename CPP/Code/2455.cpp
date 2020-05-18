#include <iostream>
using namespace std;

int main()
{
	int in, out, result, compare;
	int i = 0;
	compare = 0;
	result = 0;
	while (i<4)
	{
		cin >> out >> in;
		
		compare -= out;
		if (compare > result)result = compare;
		compare += in;
		if (compare > result)result = compare;
		i++;
	}
        cout << result;
        return 0;
}
