#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct node 
{
	int n;
	struct node *next;
};
struct node *odd=NULL;
struct node *even =NULL;
void reverse_list(struct node *p)
{
	if (p==NULL)
	return;
	reverse_list((*p).next);
	printf("%d \n", (*p).n);
}
void diff(struct node *h)
{
	struct node *li;
	struct node *cu;
	while (h!=NULL)
	{
		struct node *link=(struct node *)malloc(sizeof(struct node));
		(*link).n=(*h).n;
		(*link).next=NULL;
		if ((*h).n %2 ==0)
		{
			if (even ==NULL)
			{
				even =link;
				h=(*h).next;
				continue;
			}
			else
			{
				cu=even;
				while ((*cu).next!=NULL)
					cu=(*cu).next;
				(*cu).next=link;
			}
			h=(*h).next;
		}
		else
		{
			if (odd==NULL)
			{
				odd =link;
				h=(*h).next;
				continue;
			}
			else
			{
				cu=odd;
				while ((*cu).next!=NULL)
					cu=(*cu).next;
				(*cu).next=link;
			}
			h=(*h).next;
		}
	}
	printf ("The list containing the odd elements  \n: ");
	while (odd!=NULL)
	{
		printf("%d \n ",(*odd).n);
		odd=(*odd).next;
	}
	printf ("The list containing the even elements  \n: ");
	while (even!=NULL)
	{
		printf("%d \n ",(*even).n);
		even=(*even).next;
	}	
	
}
int main()
{
	struct node *q=NULL;
	struct node *head=NULL;
	int i;
	printf("Enter a sequence of positive integral numbers one by one , to terminate enter a number less than 1: \n");
	for (i=0;;i++)
	{
		struct node *p;
		p=(struct node *)malloc(sizeof(struct node *));
		int a;
		scanf("%d",&a);
		if (a<1)
		{
			break;
		}
		(*p).n=a;
		if (i==0)
		{
			head=p;
			q=p;
		}
		if (i==1)
		{
			(*head).next=p;
		}
		(*q).next=p;
		q=p;
	}
	struct node *w=head;
	struct node *e=head;
	struct node *r=head;
	struct node *t=head;
	printf ("You have entered %d numbers, which are displayed sequentially below : \n",i);
	while (w!=NULL)
	{
		printf("%d \n",(*w).n);
		w=(*w).next;
	}
	int max=0;
	int min =1000;
	float s=0.0;

	while (e!=NULL)
	{
		s+=(*e).n;
		if ((*e).n > max)
		{
			max=(*e).n;
		}
		if ((*e).n < min)
		{
			min=(*e).n;
		}
		e=(*e).next;
	}
	printf("You have entered %d elements. \n" ,i);
	printf("The largest number that you entered is : %d \n ",max);
	printf("The smallest number that you entered is : %d \n ",min);
	printf("The mean of all the numbers that you entered is : %f \n",(s/i));
	printf("The list printed in reverse is : \n");
	reverse_list(head);
	int ce=0;
	int co=0;
	diff(t);
}

