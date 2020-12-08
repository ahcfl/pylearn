# include <stdio.h>

int main(void)
{
	int i;
	
	scanf("m%d", &i); //m123 正确的输入  123是非法的输入
	printf("i = %d\n", i);

	return 0;
}