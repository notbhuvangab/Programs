#include <iostream>
#include <conio.h>
using namespace std;
int fac(int n)
{
 if (n==1) return 1;
 else
 {
     return n*fac(n-1);
 }
}

int main()
{
     int n;
     cout<<"Enter the Number:";
     cin>>n;
  cout<<"The factorial of "<<n<<" is:"<<fac(n);
  return 0; 
}