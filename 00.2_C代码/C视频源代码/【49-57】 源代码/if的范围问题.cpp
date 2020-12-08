# include <stdio.h>

int main(void)
{
	if (1 > 2)
		printf("AAAA\n");
		printf("BBBB\n");

	return 0;
}
/*
	在Vc++6.0中的输出结果是:
---------------------
BBBB
---------------------
	总结:
		if默认的只能控制一个语句的执行或不执行
*/