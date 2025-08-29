'''
problem:
given heads of two sorted linked lists "list1" and "list2"

Merge both lists into one sorted list.
The new list should be made by 
splicing together the nodes of the first two lists

Return the head of the merged linked list
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Optimal solution
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0, None)
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next

        elif list2.val <= list1.val:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    # now, one of the lists might still be populated
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next