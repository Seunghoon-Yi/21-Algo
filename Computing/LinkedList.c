# include <stdio.h>
# include <stdlib.h>

typedef struct nodeType Node;
struct nodeType{
    int val;
    Node* next;
};

Node* createNode(int x){
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->val = x;
    newNode->next = NULL;
    return newNode;
}
// 위가 python의 __init__과 비슷한 역할을 함.

typedef struct listType SLL;
struct listType{
    Node* first;
    //Node* tail;
    int size;
};

//functions//
void addfirst(SLL* LL, int n);
int getfirst(SLL* LL);
int getsize(SLL* LL);
void printSLL(SLL* LL);
Node* searchNode(SLL* LL, int x);
void deleteNode(SLL* LL, int x);
/////////////

int main_(void){
    SLL myLL = {NULL, 0};
    addfirst(&myLL, 10);
    addfirst(&myLL, 20);
    addfirst(&myLL, 30);
    //printf("first val = %d", myLL[0].val); 에러가 남
    printf("first val = %d \n", myLL.first->val);
    printf("second val = %d \n", myLL.first->next->val);
    printf("first val = %d \n", getfirst(&myLL));
    printSLL(&myLL);
}


int main(void){
    SLL myLL = {NULL, 0};
    addfirst(&myLL, 10);
    addfirst(&myLL, 20);
    addfirst(&myLL, 30);
    addfirst(&myLL, 50);
    printSLL(&myLL);
    deleteNode(&myLL, 20);
    printSLL(&myLL);
    deleteNode(&myLL, 40);
    printSLL(&myLL);
    deleteNode(&myLL, 50);
    printSLL(&myLL);

    return 0;
}


void addfirst(SLL* LL, int n){
    Node* newfirst = createNode(n);
    newfirst->next = LL->first; // newfirst->next = NULL
    LL->first = newfirst; //LL의 first가 newfirst를 가리키게.
    LL->size++;
}

Node* searchNode(SLL* LL, int x){
    Node* curr = LL->first;
    while (curr!=NULL){
        if(curr->val == x){
            return curr;
        }
        curr = curr->next;
    }
    return NULL;
}

void deleteNode(SLL* LL, int x){
    Node* addrToDelete = searchNode(LL, x); // LL은 이미 myLL의 주소
    Node* curr = LL->first;
    Node* prev = NULL;

    while(curr != NULL){
        if(curr->val == x){
            // printf("is same? %d", curr==addrToDelete); 참이 나와야 함.
            if(curr == LL->first){ // curr=First이면 prev는 없어도 됨
                LL->first = curr->next;
            }
            else{ // curr이 first 아니면 prev->next = curr->next
                prev->next = curr->next;
            }
            free(curr);
            LL->size--;
            return;
        }
        else{ // prev/curr를 하나씩 올리기(prev는 curr로, curr는 다음 포인터로 덮어씌움)
            prev = curr;
            curr = curr->next;
        }
    }
}

int getfirst(SLL* LL){
    if (LL->first != NULL){
        return LL->first->val;
    }
}

int getsize(SLL* LL){
    return LL->size;
}

void printSLL(SLL* LL){
    Node* curr = LL->first; // iterator
    printf("size : %d, firstval : %d \t", getsize(LL), getfirst(LL));
    while(curr != NULL){
        printf("%d ->", curr->val);
        curr = curr->next;
    }
    printf("END \n");
}