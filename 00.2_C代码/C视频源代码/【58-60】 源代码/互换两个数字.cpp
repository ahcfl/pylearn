# include <stdio.h>

int main(void)
{
	int i = 3;
	int j = 5;
	int t;  //定义临时变量

//6和7行代码无法完成i和j的互换
//	i = j;  // 6行		i = 5; j = 5; 
//	j = i;  // 7行		i = 5; j = 5;

	//正确的互换i和j的方法
	t = i;
	i = j;
	j = t;

	printf("i = %d, j = %d\n", i, j);

	return 0;
}