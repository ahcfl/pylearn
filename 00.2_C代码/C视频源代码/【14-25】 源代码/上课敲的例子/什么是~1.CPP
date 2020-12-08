# include <stdio.h>

int main(void)
{
	int i;

	i = 3;  //3最终是存放在内存中，程序终止之后3所占的空间被释放掉
	printf("i = %d\n", i);

	return 0;
}