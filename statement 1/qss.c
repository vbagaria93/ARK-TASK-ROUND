#include <stdlib.h>
#include <stdio.h>

typedef struct stringData {
    char *s;
    struct stringData *next;
} Node;

Node *createNode(char *s) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->s = s;
    newNode->next = NULL;
    return newNode;
}


void insert(Node **link, Node *newNode) {
    newNode->next = *link;
    *link = newNode;
}

void printList(Node *head) {
    while (head != NULL) {
        printf("%s\n", head->s);
        head = head->next;
    }
}



int main(void)
{
    Node *head = NULL;
    Node *tail = NULL;
    Node *n;

    n = createNode("B");
    // First node at start of list - head is updated.
    insert(&head, n);
    // First node is also the tail.
    tail = n;

    n = createNode("A");
    // Insert node at start of list - head is updated.
    insert(&head, n);

    n = createNode("C");
    // Insert node at end of list.
    insert(&tail->next, n);
    // Update tail.
    tail = n;

    printList(head);
    return 0;
}
