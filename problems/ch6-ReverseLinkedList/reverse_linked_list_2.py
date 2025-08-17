'''
problem:
Given the head of a singly linked list, and
two integers "left" and "right" where left <= right,
reverse the nodes of the list from the position left to right
return the reversed list (ie. its head)

----------------------------

input:
head = [1,2,3,4,5], left=2, right=4
output:
[1,4,3,2,5]

input:
head = [5], left=1, right=1
output:
[5]

edge cases:
head = [1,2,3,4,5], left=3, right=3
output:
[1,2,3,4,5]

head = [1,2,3,4,5], left=1, right=5
output:
[5,4,3,2,1]
----------------------------
DSA:
reverse the linked list, in-place
----------------------------
pseudocode:
initialize:
    next := null
    current := head
    previous := null
    position := 1

begin iterating over the linked list
(ie. while current)
    next = current.next

    if our position is within the range of [left, right]
    (ie. position >= left and position <= right)
        # do the reversing
        current.next = previous

    # otherwise, no processing to be done
    # move on
    previous = current
    current = next
    position += 1

return current

----------------------------
RUN THROUGH SAMPLE INPUT:
input:
head = 1->2->3->4->5, left=2, right=4

1. next=null, current.val=1, current.next=2 previous=null, position=1
    next=current.next
        =2
    1>2, no
    move on,
    previous=current
        previous.val=1
        previous.next=2
    current=2
        current.val=2
        current.next=3
    position=2

    1->2->3->4->5

2. next=2, current.val=2, current.next=3, previous=1, position=2
    next=3
    2>=2, yes
    2<=4, yes
        current.next=previous
                    =1
        1->2| 3->4->5
        ^---


SIMPLIFY THE PROBLEM:
-say that we want to reverse the whole linked list
-what do we do?
    next = current.next
    current.next = previous
    (ie. 2 points backwards to 1)

    # done processing, move on previous
    previous = current
    current = next
    position += 1

this creates an isolated cycle, 1<->2, 3->4->5



'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        next = None
        current = head
        previous = None
        position = 1

        while current != None:
            next=current.next

            if position >= left and position <= right:
                current.next=previous

            previous = current
            current = next
            position += 1
        
        return current



def main():
    # Given array
    values = [1, 2, 3, 4, 5]

    # Create the linked list
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next 

    
    print(reverseBetween(current, 2, 4))

main()


'''


'''