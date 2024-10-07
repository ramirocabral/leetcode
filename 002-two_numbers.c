#include <stdbool.h>

void insertList (struct ListNode**,struct ListNode**, int );


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){

    struct ListNode *l3 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode *tail = l3;

    l3->val = 0;
    l3->next = NULL;

    bool carry= false;

    while ((l1 != NULL) || (l2 != NULL) || (carry == true)) {
        tail->val = 0;
        
        if (l1 != NULL) {
            tail->val += l1->val;
            l1 = l1->next;
        }
        if (l2 != NULL){
            tail->val += l2->val;
            l2 = l2->next;
        }
        if (carry == true){
            tail->val += 1;
        }
        if (tail->val > 9){
            carry = true;
            tail->val = tail->val % 10;
        }
        else
            carry = false;
        if(l1 != NULL || l2!=NULL || carry == true){
            tail->next = malloc(sizeof(struct ListNode));
            tail->next->next=NULL;
            tail = tail->next;
        }
    }
    return l3;
}
