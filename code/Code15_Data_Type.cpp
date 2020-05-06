#include <iostream>
using namespace std;
int main()
{
int num1 = 5, num2 = 4;
double num3;

// 명시적 변환을 하지 않는 경우
num3 = num1 / num2;
cout << "강제 변환을 하지 않으면 5/4 의 결과는" << num3 << "입니다" << endl;

// 캐스트 연산자 사용하여 명시적 변환을 하는 경우
num3 = (double)num1 / (double)num2;
cout << "강제 변환을 하면 5/4 의 결과는" << num3 << "입니다" << endl;


return 0;

}
