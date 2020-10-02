#include<stdio.h>
#include<stdlib.h>

typedef struct node
{
	int data;
	struct node *next;
}node;
int main()
{
	int a , i = 1 , n,pos;
	node *p,*q,*head,*temp,*prevnode,*newnode;
	printf("Enter the number of nodes");
	scanf("%d",&n);

	printf("Enter node %d  \n",i);
	p = (node*)malloc(sizeof(node));
	scanf("%d",&a);
	p->data = a;
	p->next = NULL;
	head = p;

	for(i=2;i<=n;i++)
	 	{
	 		printf("Enter node %d  \n",i);
		 	q = (node*)malloc(sizeof(node));
			scanf("%d",&a);
			q->data = a;
			q->next = NULL;
		 	p->next = q;
		 	p = p->next;

		}

	p = head;
	while(p!=NULL)
	{
		printf("\t %d", p->data);
		p = p->next;
	}
	printf("\nINSERTING A NODE AT ANYWHERE");
	printf("\nGive a position\n");
	scanf("%d",&pos);
	if(pos>n)
    {
        printf("INVALID");
    }
    else
    {
        newnode = (node*)malloc(sizeof(node));
        temp = head;
        while(i<pos)
        {
            prevnode = temp;
            temp = temp->next;
            i++;
        }
        printf("Give a value");
        scanf("%d",&a);
        newnode->data=a;
        newnode->next=temp;
        prevnode->next=newnode;


    }
    p=head;
	while(p!=NULL)
	{
		printf("\t %d", p->data);
		p= p->next;
	}
}
