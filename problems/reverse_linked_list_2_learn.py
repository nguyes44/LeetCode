from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    # Sample input: head = [1,2,3,4,5], left=2, right=4
    dummy = ListNode(0, head)

    # 1) Reach node at position left
    leftPrev = dummy # the node just before the sublist
    current = head  # going to be the initial head of the sublist
                    # ie. 2

    for i in range(left - 1):
        # move leftPrev and current to their positions
        leftPrev = current
        current = current.next


    # 2) Reverse from left to right
    prev = None # the tail of the FINAL sublist
                # ex. first iteration, 2 -> None
                # second, 3 -> 2 -> None
    for i in range(right - left + 1):
        next = current.next # save the next for later, typical
        current.next = prev # now, 2 points to None
                            # 2nd iteration, 

        # move on both pointers
        prev = current #1st iteration, prev goes from None to 2
        current = next #1st iteration, current goes from 2 to 3


    # 3) Reattach the sublist
    # this seems like black magic, but the visualization helps
    leftPrev.next.next = current 
    leftPrev.next = prev

    return dummy.next