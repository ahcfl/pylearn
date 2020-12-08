void f(void)
{
	void g(int i)
	{
		int k(void)
		{
			.....
			return 10;
		}
	}
}

void f()
{
	g(5);
}

void g(int i)
{
	k();
}
	