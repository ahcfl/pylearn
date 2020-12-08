# include <stdio.h>

int main(void)
{
	int i, j;

	printf("请输入i的值(中间以空格分隔): ");
	scanf("%d %d", &i, &j);
	printf("i = %d, j = %d\n", i, j);

	return 0;
}