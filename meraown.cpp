#include<iostream>
#include<conio.h>
using namespace std;

struct Node
{
    int data;
    Node* next;
};

Node* head ;
void Insert(int x)
{
    Node* temp = new Node();
    temp->data=x;
    temp->next=NULL;
    head = temp;
}
void Print()
{
    Node* temp = head;
    while(temp->next != NULL)
    {
        cout<<temp->data;
        temp = temp->next;
    }
    cout<<endl;
}
int main()
{
    head = NULL;
    int i,n,x;
    cout<<"Enter the number of elements";
    cin>>n;
   for(i=0;i<n;i++)
   {
     cout<<"Enter the element:";
     Insert(x);
     Print();
   }
   return 0;
}