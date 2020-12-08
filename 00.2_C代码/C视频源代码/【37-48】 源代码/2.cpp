# include <stdio.h>

int main(void)
{
	int i;

	//scanf("%d\n", &i);  //非常不好的格式, 不要加 \n
	scanf("%d", &i);
	printf("i = %d\n", i);

	return 0;
}