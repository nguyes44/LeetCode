'''
Problem:
Given the head of a singly linked list, return the middle node of the linked list

If there are two middle nodes, return the second middle node

Ex. 
input: 1 - 2 - 3 - 4 - 5
output: 3

input: 1-2-3-4-5-6
output: 4, since its the second middle node


Possible DSA & Sol:
We can use the two pointer approach, different paces
This is often used to find the things related to length of an iterable.

Pseudocode:
-initialize two pointers; fast and slow, which move at 1 and 2 paces respectively
-begin iterating over linked list
-once the fast pointer has reached the end, 
    we know that the slow pointer is at the middle, 
    since it has moved half the distance

return the slow pointer node

'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # since we need to check if fast has reached it's end,
        # and if we can perform fast.next.next
            # without this check, say we were at the last node
            # we would enter the loop, but we can't actually safely call fast.next.next
            # this would be null.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    

'''
What about the second middle shenanigans?
1 2 3 4 5 6
Here, there are 2 middles
Both start at 1
slow -> 2
fast -> 3
--
slow -> 3
fast -> 5
--
slow -> 4
fast -> null

now, fast is null. Return 4.
----

Time complexity:
The algorithm terminates once the fast pointer reaches the end.
The fast pointer will reach the end in O(N/2) time.
=> O(N)

Space complexity:
we only initialize 2 pointers. Independent of the linked list size
=> O(1)
'''