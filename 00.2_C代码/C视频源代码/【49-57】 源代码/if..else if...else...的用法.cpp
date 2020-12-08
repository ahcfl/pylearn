/*
	2009年10月16日10:06:00
	一定要明白改程序为何会编译出错
*/

# include <stdio.h>

int main(void)
{
	double delta = -1;

	if (delta > 0)
		printf("有两个解!\n");
		printf("哈哈!\n");
	else if (delta == 0)
		printf("有一个唯一解!\n");
	else
		printf("无解!\n");

	return 0;
}