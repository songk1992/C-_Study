// CPP 그림판
//출처 https://www.youtube.com/watch?v=OF1mWXureOw

#include <stdio.h>
#include <dos.h>
#include <Graphics.h>
#include <conio.h>


union REGS in, out;
int callmouse()
{
	in.x.ax = 1;
	int86(51, &in & out);
	return 1;
}

void mousepos i(int& xpos, int& ypos, int& click)
{
	in.x.ax = 3;
	int86(51, &in, &out);
	click = out.x.bx;
	xpos = out.x.cx;
	ypos = out.x.dx;
}

void setpos i(int& xpos, int& ypos)
{
	in.x.ax = 4;
	in.x.cx = xpos;
	in.x.dx = ypos;
	int 86(51, &in, &out);

}

int main()
{
	int x, y, cl, a, b;
	clrscr();
	int d = 0, m;
	initgraph(&d, &m, "c:\\turboc3\\bgi");
	a = 100;
	b = 400;
	setposi(a, b);
	callmouse();
	int i;
	do
	{
		mouseposi(x, y, cl);
		if (cl == 1)
			lineto(x, y);
		gotoxy(1, 1);
		cout << "Mouse position is" << x << y << endl;
		cout << "Clcik : " << cl << endl;
		cout << "Press any key to hide the mouse" << endl;
	} while (!kbhit());
	getch();
	cout << "Press any key to Exit";
	getch();
}

