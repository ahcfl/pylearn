/*
	对枚举的应用!
*/
# include <stdio.h>

enum weekday
{
	MonDay, TuesDay, WednesDay, ThursDay, FriDay, SaturDay, SunDay //考虑将WednesDay改为WednesDay = 5之后，MonDay与SunDay的值是多少？
};

void f(enum weekday i) //本函数的目的只是期望接受0～6之间的数字，将形参i定义为枚举型，可以有效的避免传参失误的问题
{
	switch (i)
	{
	case 0:
		printf("MonDay!\n");
		break;
	case 1:
		printf("TuesDay!\n");
		break;
	case 2:
		printf("WednesDay!\n");
		break;
	case 3:
		printf("ThursDay!\n");
		break;
	case 4:
		printf("FriDay!\n");
		break;
	case 5:
		printf("SaturDay!\n");
		break;
	case 6:
		printf("SunDay!\n");
		break;  
	}          
}

int main(void)
{
	f(FriDay); //虽然FriDay本质上就是5，但直接写成f(5);就是错的， 也不能写成f(10); 考虑为什么！ 嘿嘿

	return 0;
}