# include <stdio.h>


//max是函数的名字, i和j是形式参数，简称形参 void表示函数没有返回值
void max(int i, int j)
{
	if (i > j)
		printf("%d\n", i);
	else
		printf("%d\n", j);
}

int main(void)
{
	int a, b, c, d, e, f;

	a = 1, b = 2; c = 3, d = 9, e = -5, f = 100;
	max(a, b);
	max(c, d);
	max(e, f);
/*
	if (a > b)
		printf("%d\n", a);
	else
		printf("%d\n", b);

	if (c > d)
		printf("%d\n", c);
	else
		printf("%d\n", d);
	
	if (e > f)
		printf("%d\n", e);
	else
		printf("%d\n", f);
*/
	return 0;
}