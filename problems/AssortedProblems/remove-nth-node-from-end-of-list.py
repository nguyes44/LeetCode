'''
problem:
given the head of a linked list,
remove the nth node from the end of the list
return the new linked list's head

------------------------------------
input/output:

head = [1,2,3,4,5], n=2
output:
[1,2,3,5]
expl:
we want to remove the 2nd last node (ie. 4)

head=[1], n=1
output: []

head=[1,2], n=1
output: [1]

------------------------------------
custom input/output:
head=[1,2,3,4,5], n=5
output: [2,3,4,5]

------------------------------------
initial thoughts:
- we know n=2 means we have to remove the 2nd last node
- however, we start at the head.
- we have no clue how long the list is
- might be able to use fast/slow pointers to determine length (?)

------------------------------------
brute force pseudocode:
- start at the head
- iterate until the end of the list,
    counting how long the list is
- begin replacement
    move 2nd_iter to length - n
    2nd_iter.next = initial_iter
- return head (dummy val.next)


looking @ edge case of head=[1], n=1
    if length == 1:
        2nd_iter.next = None

    return 2nd_iter.next
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        initial_iter = dummy
        length = 0

        while initial_iter.next != None:
            initial_iter = initial_iter.next
            length += 1

        # edge case of length = 1,
        # => n=1, so we return nothing
        if length == 1:
            return None

        # now, we want to move 2nd_iter to length - n
        second_iter = dummy
        for i in range(length-n):
            second_iter = second_iter.next

        # begin replacement
        if n == 1: # removing the right-most node
            second_iter.next = None
        elif (length-n) == 0: # removing the left most node
            return second_iter.next.next
        else:
            second_iter.next = second_iter.next.next

        return dummy.next
    

'''
failed test case:
head = [1,2], n=1

head=[1,2,3], n=3

head=[1,2,3,4,5,6,7,8,9,10], n=7

------------------------------------
time complexity:
- iterate to find length, N
- move second_iter (length-n)
    worst case, N
=> O(2N) = O(N)

space complexity:
- O(1)

------------------------------------
improvements:
- one pass is possible
- was thinking of doing fast/slow pointer
    fast: finds the length
    slow: keeps reference pointer for replacement

- problem arises when slow pointer 
    passes where its supposed to be
    (ie. right before the removed node)
- we dont know len until we're at the end,
    so we're afraid of moving the slow pointer past intended point
- but we'd also like to progress the slow pointer
    since this is one pass

given n = 7, 
    we know the list is AT LEAST 7 nodes long
    => we can move the slow pointer n/2 = 7/2 = 3 (rounded down)
    nodes and not pass the node to be removed

- is this true?
- is this too scared of a heuristic?
    -in 1st case, we'd have to still move slow 
    up 2 nodes

------------------------------------

- what if i iterate n times, then create a pointer at head
    then, begin iteration of both until p1 reaches the end

- then perform replacement as usual

GO THROUGH EDGE CASES w/ THIS

'''

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    p1 = dummy

    # move p1 until n
    for i in range(n):
        p1 = p1.next

    p2 = dummy
    length = n

    # now, move both p1 and p2 
    # until p1 reaches end
    while p1.next != None:
        p1 = p1.next
        p2 = p2.next
        length += 1
    
    # p2 will be at the node 
    # right before removal node
    # perform removal 
    if length == n and length == 1:
    # ie. trivial list
        dummy.next = None
    elif length == n:
    # ie. removing left-most
        dummy.next = p2.next.next
    elif n == 1: 
    # ie. removing right-most
        p2.next = None 
    else:
    # ie. removing intermediate
        p2.next = p2.next.next

    return dummy.next

'''
time complexity:
- move p1 n times
- then, move p1 AND p2 until end
=> we only iterate once
O(N)

space complexity:
- O(1)
'''