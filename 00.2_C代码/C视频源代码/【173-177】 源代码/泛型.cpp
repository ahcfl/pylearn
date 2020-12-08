int a[10] = {.....};
int * pH = a;

for (i=0; i<10; ++i)
{
	printf("%d\n", *pH);
	pH++;
}