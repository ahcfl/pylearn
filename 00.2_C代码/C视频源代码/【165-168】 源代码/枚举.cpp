# include <stdio.h>

//只定义了一个数据类型，并没有定义变量， 该数据类型的名字是 enum WeekDay
enum WeekDay
{
	MonDay, TuesDay, WednesDay, ThursDay, FriDay, SaturDay, SunDay
};

int main(void)
{
	//int day; //day定义成int类型不合适
	enum WeekDay day = SunDay;
	printf("%d\n", day);

	return 0;
}