#include <iostream>
using namespace std;

 class RESORT
 {   public:
     int Rno;
     char Name[20];
     float charges;
     int days;
     float COMPUTE();
   
   void Getinfo();
   void Dispinfo();
 };
 void RESORT::Getinfo()
 {
     cin>>Rno;
     gets(Name);
     cin>>charges>>days;
 }
 void RESORT::Dispinfo()
 {
    cout<<Rno<<endl<<Name<<endl<<charges<<endl<<days<<endl;
    cout<<"Total Amount:";
    cout<<COMPUTE()<<endl;
 }
 float RESORT::COMPUTE()
 {
     float  amount = charges*days;
      if(amount>11000)
          amount=1.02*days*charges;
    return amount;      
 }
 
int main()
{
    RESORT a;
    cout<<"Enter the Details:";
    a.Getinfo();
    cout<<"The Billed details are:";
    a.Dispinfo();
    return 0;
}


