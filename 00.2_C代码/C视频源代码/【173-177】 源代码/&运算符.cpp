# include <stdio.h>

int main(void)
{
	int i = -5;
	int j = 10;
	int k;

	k = i & j;
	printf("%d\n", k);

	k = i && j; //k的值只能是1或0， 因为&&是逻辑运算符， 逻辑运算符的结果只能是真或假， 在C中，真用1表示看，假用零表示
	printf("%d\n", k);

	return 0;
}