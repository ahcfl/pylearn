# include <stdio.h>

void f(void)
{
	int i;

	for (i=0; i<5; ++i)
	{
		printf("大家辛苦了!\n");
		return;
	}
	printf("同志们好!\n");
}

int main(void)
{
	f();

	return 0;
}