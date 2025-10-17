'''
problem:
given the root of a binary tree,
return the level order traversal of its nodes' values.
(ie. from left to right, level by level)

-----------------------------------------------
pseudocode:
- we'll use BFS to traverse the tree,
this is because BFS gives us level-ordered traversal
by exploring all nodes at present level, 
then continuing to the next level

BFS pseudocode:
- mark start node
- queue it

while the queue is non-empty:
    dequeue a node
    for all its neighbours (starting with left here)
        mark them (don't think we do this here)
        queue them

'''

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if root == None:
        return []

    # native to BFS
    queue = deque()
    queue.append(root)

    # problem specific
    level_num = 0               # what level we're on
    level_cutoff = 2**level_num # the max number of nodes expected at level
    num_nodes = 0               # current number of nodes at level
    current_level = []          # current node values of level
    levels = []                 # master list of level node values

    while queue:
        # BFS native: mark current
        current_node = queue.popleft()
        if current_node == None:
            # None's neighbours are None and None for the sake of future num_nodes
            # however, the problem is that the queue will always be populated with None now.
            queue.append(None)
            queue.append(None) 
            num_nodes += 1 # still increment the hypothetical num_nodes

            if num_nodes >= level_cutoff and len(current_level) != 0:
                levels.append(current_level)
                current_level = [] # reset current level
                level_num += 1
                level_cutoff = 2**level_num
                num_nodes = 0
            continue

        # BFS native: add neighbours
        queue.append(current_node.left)
        queue.append(current_node.right)
        
        # processing current_node
        current_level.append(current_node.val)
        num_nodes += 1

        if num_nodes >= level_cutoff and len(current_level) != 0:
            levels.append(current_level)
            current_level = [] # reset current level
            level_num += 1
            level_cutoff = 2**level_num
            num_nodes = 0

    if len(current_level) > 0 and num_nodes < level_cutoff:
    # ie. if the last level did not process max num nodes, 
    # we won't be able to append the current_level 
        levels.append(current_level)

    return levels


'''
failed test case:
[3,9,20,null,null,15,7]
expected: [[3],[9,20],[15,7]]
actual: [[3,9],[20,15],[7]]

dry run:
TLDR;
- in Python, 2^0 is bitwise XOR
to perform exponentiation, do 2**0

-----------------------------------
failed test case:
[1,2]
expected: [[1],[2]]
actual: [[1]]

TLDR;
- i don't think I accomodated for cases where theres only one child
- I didn't accomodate for when we have None nodes, 
    that we might need to append to levels

dry run:
- queue = [1]
- queue = [2, None]
    current_level = [1]
    num_nodes = 1
    at cutoff, so we'll:
    - append
    - reset current level
    level_num = 1
    level_cutoff = 2
    num_nodes = 0

- queue = [None, None, None]
    current_level = [2]
    num_nodes = 1

    don't exit

- queue = [None, None]
    current_node = None
    num_nodes = 2

    at cutoff, so we'll:
    - append current_level = [2] and reset
    - level_num = 2
    - level_cutoff = 4
    - num_nodes = 0

- queue = [None]
    num_nodes = 1

- queue = []
    num_nodes = 2

failed test case:
[1]
expected = [[1]]
actual = [[1], []]

TLDR; 
- I was appending current_level after processing only None nodes
    had to ensure current_level wasn't empty

dry run:
- queue = [1]
- queue = []
current_node = 1
current_level = [1]
num_nodes = 1

reset the current level
levels = [[1]]
current_level = []
level_num = 1
level_cutoff = 2
num_nodes = 0

- queue = [None]
None, so only inc. num_nodes
    num_nodes = 1
don't exit

- queue = []
None, so only inc. num_nodes
    num_nodes = 2

-----------------------------------
failed test case:
[1,2,null,3,null,4,null,5] (ie. all left children)
expected:
[[1],[2],[3],[4],[5]]
actual:
[[1],[2],[3,4],[5]]

TLDR;
- there are so many more edge cases with graph problems that I
    didn't expect. List them all out
    ex. - all left children
    - all right children
    - only one node
    - no nodes 
- the reason why my approach adds 3 and 4 to the same level is bc
    im expecting the level 1 None to queue level 2 Nones
    How would level 1 None know to enqueue 2 Nones?
    
    I think it can always just queue up 2 Nones


dry run:
- queue = [1]
- queue = []
    current_node = 1
    queue = [None, 2]
    current_level = [1]
    num_nodes = 1

    append [1] to levels
    reset current level

- queue = [None]
    current_n = 2
    queue = [None,3,None]
    current_level = [2]
    num_nodes = 1

    don't exit

- queue = [None,3]
    current_n = N
    num_nodes = 2

    append [2] to levels
    reset current level

- queue = [None]
    current_n = 3
    queue = [None,4,None]
    num_nodes = 1
















'''