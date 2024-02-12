#include <stdio.h>
#include <stdlib.h>
typedef struct Node {
    int data;
    struct Node *next;
} node;

void insertAtBegin(node **head, int item);
void traverseInOrder(node *);
void display(node *);

int main(void)
{
    int item;
    node *head = NULL;
    int op,x=1;
    while(x==1)
    {
        printf("Enter 1 for inserting element in the begining:\n");
        printf("Enter 2 for calculating length of Linked List:\n");
        printf("Enter 3 for displaying the LinkedList:\n");
        printf("\n");
        scanf("%d",&op);
        switch(op)
        {
            case 1: printf("Enter item to insert at begining :");
                    scanf("%d", &item);
                    insertAtBegin(&head, item);
                    printf("Item inserted\n");
                    break;
            case 2: traverseInOrder(head);
                    break;      
            case 3: display(head);
                    break;
            case 0:printf("Wrong Choice");
        }
        printf("Press 1 to continue and 0 to exit: ");
        scanf("%d",&x);
    
    }
}
void insertAtBegin(node **head, int item)
{
    node *newnode = (node *)malloc(sizeof(node));
    newnode->data = item;

    if(*head == NULL)
        newnode->next=NULL;
    else
        newnode->next = *head;

    *head = newnode;

}
void traverseInOrder(node *head)
{
    int c=0;
    while(head != NULL)
    {
        c++;
       // printf(" %d ", head->data);
        head = head->next;
    }
    printf("total length: %d\n",c);
}
/*int c=1;
    while(head->next!=NULL)
        c++;
    printf("total: %d\n",c);*/


void display(node *ptr)
{
    while(ptr!=NULL)
    {
        printf("%d ", ptr->data);
        ptr=ptr->next;
    }
    printf("\n");
}
