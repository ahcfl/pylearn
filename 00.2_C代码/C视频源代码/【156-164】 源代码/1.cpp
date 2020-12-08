# include <stdio.h>

struct Student
{
	int age;
	char sex;
	char name[100];
}; //分号不能省

int main(void)
{
	struct Student st = {20, 'F', "小娟"};
	struct Student * pst = &st;
	
	printf("%d %c %s\n", st.age, st.sex, st.name);
	printf("%d %c %s\n", pst->age, pst->sex, pst->name);  //pst->age 转化成 (*pst).age 等价于 st.age

	return 0;
}