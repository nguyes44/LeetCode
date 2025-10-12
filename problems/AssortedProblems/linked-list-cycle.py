'''
problem:
Given the head of a linked list,
determine if the linked list has a cycle in it.

--------------------------
pseudocode:
- initialize a slow and fast pointer
- slow: moves 1 step at a time
- fast: moves 2 steps at a time
- if slow and fast ever meet, return true
- if fast reaches the end (ie. fast == None), return false

'''

from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

'''
time complexity:
- O(N), i think bc we have to iterate until fast meets slow

space complexity:
O(1), since we only keep 2 pointers

'''