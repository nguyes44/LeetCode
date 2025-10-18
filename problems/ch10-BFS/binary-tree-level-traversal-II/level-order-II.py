'''
problem:
Given the root of a binary tree,
return the bottom-up level order traversal of nodes' values
(ie. from left to right, 
level by level, 
from leaf to root)

---------------------------------
pseudocode:
- we should use BFS because we require level order traversal.
- first iterate using BFS
- recall: q_len defines the level length
- can we keep track of previous q_len's on a stack,
    then "process" the nodes all at once?
ex.
[3, 9, 20, N, N, 15, 7]
q_len stack = [1,2,4]
- pop 4 from q_len stack
- take 4 entries from array
    - append to list from back if not null
    => [15, 7] 
    - append to master list

- pop 2 from q_len stack
- take 2 items
    => [9, 20]

- take 1 item
=> [3]

'''

# what was the result before?
# "process" q_len times, because q_len keeps track of the level length
# what does "process" mean?
# if the node was non-null,
#   we'd append it to the level list
#   also, add its children

# on this first iteration,
# we don't append to a level list
# we do add its children

# the problem is that with this current approach,
# we add 15 and 7's children too, which are all N.
# I think we can work with this.
# since we try to add to the back if it's not None
# we can check list length at the end before adding to master list

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
    if root == None:
        return []
    
    # BFS native
    q = deque()
    q.append(root)

    # problem specific
    all_nodes_list = []
    q_len_stack = []
    levels_list = []

    while q:
        q_len = len(q)
        q_len_stack.append(q_len)

        for i in range(q_len):
            # process node from queue
            node = q.popleft()
            if node:
                all_nodes_list.append(node.val)

            if node:
            # add children if we're working with a real node
                q.append(node.left)
                q.append(node.right)

    # part 2: working with all_nodes_list = [3, 9, 20, N, N, 15, 7, N, N, N, N]
    while q_len_stack:
        num_level_items = q_len_stack.pop()
        level = []

        for i in range(num_level_items):
            if len(all_nodes_list) != 0:
                value = all_nodes_list.pop()
            if value:
                level.insert(0, value)

        if level:
            levels_list.append(level)

    return levels_list



'''
failed test case:
[3,9,20,null,null,15,7]

expected: [[15,7],[9,20],[3]]
actual: [[15,7,15,7],[9,20,9,20],[3,3],[3]]

dry run:
- 

'''
