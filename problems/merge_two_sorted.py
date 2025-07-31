'''
problem:
You are given the heads of two sorted linked lists, list 1 and list 2

Merge the two lists into one sorted list
The list shouild be made by splicing together nodes of the first two lists

Return the head of the merged linked list

ex input/output:
list1 = 1,2,4 
list2 = 1,3,4
output = 1,1,2,3,4,4

DSA:
we should use merge intervals, because we're required to
merge (potentially) overlapping intervals

Pseudocode:
initialize two pointers, one at the head of each of the linked lists

initialize a new linked list

while one of the lists still has items
    (ie. pointer1 and pointer2 not null)
    compare the two pointer values
    if pointer1.value < pointer2.value:
        append to the linked list a node w/ pointer1's value
    else, append pointer2's value

we might have nodes in the other list, 
so iterate over the non-empty list
and append to the final linked list.

return the head of the final linked list
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = list1
        pointer2 = list2
        merged_list = []

        # iterate while one of the linked lists still has items
        while pointer1 and pointer2:
            # check which node should go in the new list
            if pointer1.val < pointer2.val:
                # we know that the value that should go in is pointer1.val
                current_node = ListNode(pointer1.val, None)
                merged_list.append(current_node)
                # move the pointer of linked list 1
                pointer1 = pointer1.next
                if len(merged_list) > 1:
                    # update the previous node's .next
                    merged_list[-2].next = current_node

            else:
                # instead, the value going in is pointer2.val
                current_node = ListNode(pointer2.val, None)
                merged_list.append(current_node)
                # move the pointer of linked list 2
                pointer2 = pointer2.next
                if len(merged_list) > 1:
                    # update the previous node's .next
                    merged_list[-2].next = current_node

        # at this point, one of the linked lists is still empty.
        # determine which one, and append all of its nodes to merged_list
        while pointer1:
            current_node = ListNode(pointer1.val, None)
            merged_list.append(current_node)
            if len(merged_list) > 1:
                merged_list[-2].next = current_node
            pointer1 = pointer1.next

        while pointer2:
            current_node = ListNode(pointer2.val, None)
            merged_list.append(current_node)
            if len(merged_list) > 1:
                merged_list[-2].next = current_node
            pointer2 = pointer2.next    
        
        if not merged_list:
            return None
        return merged_list[0]
    
'''
Why is this memory exceeded?

in the second loop, 
    merged_list[-2].next = pointer1
this is a reference to the existing node.
so im rewriting the original node's .next


also, -2 assumes there is more than 2 elements in your list
we can change the condition to if len > 1, make the new fix


I also didn't account for the case where merged_list can be empty, so 

what problems arose from this question?
-reusing old nodes. provide an example of what to do vs. what not to do
-my approach used a list of nodes. this was unnecessary?
-edge case analysis, i got tilted on index out of ranges (ie. -2, 0)
-look at the optimal solution


'''