from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    current = head
    left_previous = dummy

    #1. get the nodes at left and immediately before left
    for i in range(left - 1):
        left_previous = current
        current = current.next


    previous = None
    #2. reverse the sublist
    for i in range(right - left + 1):
        next = current.next     # store the next node temporarily
        current.next = previous # cut the existing link and reverse

        previous = current      # update previous as we just processed
        current = next          # update current to next
    
    #3. reconnect the sublist
    left_previous.next.next = current # the end of the linked list
    left_previous.next = previous

    return dummy.next