#include<iostream>
#include<process.h>
using namespace std;
struct Node
{
    int info;
    Node* next;
}*start,*newptr,*save,*ptr;

Node* create_new_node(int);
void insert_beg(Node*);
void Display(Node*);

int main()
{
    start = NULL;
    int inf;
    char ch = 'y';
    while (ch == 'y'|| ch == 'Y');
  {
      system("cls");
      cout<<"\n Enter information for the new node...";
      cin>>inf;
      cout<<"\n Creating new node!! Press enter to continue";
      system("pause");
      newptr = create_new_node(inf);
      if( newptr != NULL)
      {
          cout<<"\n\n New node Created Successfully. Press Enter to continue";
          system("pause");
      }
      else
      {
          cout<<"\n Cannot create New Node!! Aborting\n";
          system("pause");
          exit(1);
      }
    cout<<"Now inserting this node in the beginning of the list\n";
    cout<<"Press Enter to continue";
    system("pause");
    insert_beg(newptr);
    cout<<"\n Now the list is :\n";
    Display(start);
    cout<<"\n Press Y to enter more nodes, N to exit...\n";
    cin>>ch;
  }
return 0;
}
Node* create_new_node(int n)
{
    ptr = new Node;
    ptr->info = n;
    ptr->next = NULL;
    return ptr;
}
void insert_beg(Node* np)
{
    if(start = nullptr)
      start = np;
    else
    {
      save = start;
      start = np;
      np->next = save;
    }
}
void Display(Node* np)
{
   while (np!= nullptr)
   {
       cout<<np->info<<"->";
       np = np->next;
   }
   cout<<"!!!\n";
}
