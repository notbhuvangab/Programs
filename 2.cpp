#include <iostream>
using namespace std;
#define MULT(x,y) x*y
inline int mult(int x,int y)
{
    return x*y;
}

int main()
{
    int i=2,j=3;
    cout << MULT(MULT(i,j-1),i) << " ";
    cout << MULT(i,MULT(i,j-1)) << " ";
    cout << mult(mult(i,j-1),i) << " ";
    cout << mult(i,mult(i,j-1)) << endl;

   return 0;

}