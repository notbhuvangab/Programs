#include <iostream>
int fun(int x)
{
    return x;
}

int fun(int x,int y)
{
    return x+y;
}

int fun(int x,int y = 10)
{ 
    return x+y;
}

int main()
{
    fun(10);
    fun(10,20);
    return 0;
}