#include <iostream>
#include <stdlib.h>
#include <time.h>

inline int randCoin() { return rand() % 2; }
inline int randDice() { return rand() % 6 + 1; }
inline char randLChar() { return rand() % 24 + 'a'; }
inline char randUChar() { return rand() % 24 + 'A'; }
inline char randNum() { return rand() % 10 + '0'; }

void main()
{
	srand((unsigned)time(NULL));
	std::cout << "coin  dice  LChar  UChar  Num\n";
	for (int i = 0; i < 6; i++)
	{
		std::cout << "  " << (randCoin() == 0) ? "head" : "tail";
		std::cout << "  " << randDice();
		std::cout << "  " << randLChar();
		std::cout << "  " << randUChar();
		std::cout << "  " << randNum()<<std::endl;
	}

}
