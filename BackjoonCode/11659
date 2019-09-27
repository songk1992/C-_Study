#include <iostream>

int main()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);


	int N, M, a, b, sum;
	int array[100000] = { 0, };

	std::cin >> N >> M;
	for (int i = 1; i < N + 1; i++)
	{
		std::cin >> array[i];
		array[i] += array[i - 1];
	}
	/*
	for (int i = 0; i < N+1; i++)
	{
	std::cout << " " << i << "th " << array[i];
	}
	std::cout << "\n";
	*/

	for (int i = 0; i < M; i++)
	{
		std::cin >> a >> b;
		/*
		std::cout << " r1 is " << a << " array is" << array[a] << "  ";
		std::cout << " r2 is " << b << " array is" << array[b] << "  ";
		*/
		sum = array[b] - array[a - 1];
		std::cout << sum;
		if(i<M-1)
		std::cout << "\n";
	}
}
