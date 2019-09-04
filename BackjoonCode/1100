<pre><code>#include <iostream>
#include <string>
using namespace std;


int main()
{
	int count = 0;

	for (int i = 0; i < 8; i++)
	{
		char arr[7];
		for (int j = 0; j < 8; j++)
		{
			cin >> arr[j];

			//홀수 라인
			if ((i+1)%2==0)
			{
				if ((j + 1) % 2 == 0)
				{
					if (arr[j] == 'F') count++;
				}
			}
			//짝수라인
			else if(i%2==0)
			{
				if ((j) % 2 == 0)
				{
					if (arr[j] == 'F') count++;
				}
			}
		}
	}
	cout << count;
}
</code></pre>
