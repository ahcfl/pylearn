# include <stdio.h>

int main(void)
{
	char ch = 'A';  //4行    OK  等价  char ch;  ch = 'A';
//	char ch = "AB";  //error 因为"AB"是字符串， 我们不能把字符串赋给单个字符变量
//	char ch = "A";   //error
	
//	char ch = 'AB'; //'AB'是错误的

//	char ch = 'B';  //error, 因为ch变量已经在4行定义了， 这样会导致变量名被重复定义

	ch = 'C';
	ch = 'D';
	printf("%c\n", ch);


	return 0;
}