// 21 - Merge Two Sorted Lists
// Runtime = 0ms, Beats = 100%

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    if(!list1 && !list2) return NULL;
    struct ListNode head;
    struct ListNode *temp = &head;
    while (list1 && list2) {
        if(list1->val > list2->val) {
            temp->next = list2;
            list2 = list2->next;
        }
        else {
            temp->next = list1;
            list1 = list1->next;
        }
        temp = temp->next;
    }
    while(list1) {
        temp->next = list1;
        list1 = list1->next;
        temp = temp->next;
    }
    while(list2) {
        temp->next = list2;
        list2 = list2->next;
        temp = temp->next;
    }
    return head.next;
}
