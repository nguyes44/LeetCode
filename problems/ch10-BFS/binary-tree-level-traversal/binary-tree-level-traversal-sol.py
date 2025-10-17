'''
notes:
- the largest a level can be (for a binary tree) is n/2
    therefore, the worst case memory is O(n/2) => O(n)
TLDR;
- inside the while loop, 
    define q_len and "process" ALL nodes q_len times
    (ie. append to level and add children if possible)
    q_len predefines the level length
'''
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    res = []

    q = deque()
    q.append(root)

    while q:
        q_len = len(q)
        level = []

        # this is the part I don't understand
        # why q_len?
        for i in range(q_len):
            node = q.popleft()

            # don't add None nodes to level
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)

        if level:
            res.append(level)

    return res