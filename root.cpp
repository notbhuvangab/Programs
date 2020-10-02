#include <iostream>
#include <math.h>
int main()
{
    using namespace std;
    float a,b,c;
    cout<<"Equation is of the format ax²+bx+c=0"<<endl;
    cout<<"Enter a:";
    cin>>a;
    cout<<"Enter b:";
    cin>>b;
    cout<<"Enter c:";
    cin>>c;
    cout<<"solution of equation is equal to:"<<endl;
    cout<<"x1="<<(((-b)+ sqrt(pow(b,2)-4*a*c))/2*a)<<endl;
    cout<<"x2="<<(((-b)- sqrt(pow(b,2)-4*a*c))/2*a);
    return 0;
} 