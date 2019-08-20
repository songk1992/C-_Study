#include <iostream>
#include <time.h>
using namespace std;

int main()
{
int num, i, data;
srand(time(NULL));
num = rand() % 10;

i = 1;
cout << " 0 부터 9 사이의 숫자를 입력하고 엔터 치시오"<<endl;

while(1)
{
cout << "["<< i << "]번째 도전" << endl;
cin >> data;

if (data < num)
cout << data << "보다 큽니다" << endl;
else if (data > num)
cout << data << "보다 작습니다" << endl;
else
{
cout << "Correctomundo " << i << " 번째에 맞혔군요" << endl;
break;
}
i++;

}

}
