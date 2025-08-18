'''
Problem:
Implement a FIFO queue using only two stacks.
Support push, peek, pop, and empty
void push(int x) - push an element X to the back of the queue
int pop() - remove the element from the front of the queue and return it
int peek() - return the element at front of queue
boolean empty() - return true if the queue is empty. False otherwise

-------------------------------
pseudocode:
void push(int x):
    - read the top most element from 1st stack, push that to 2nd stack
    - push x into the 1st stack
    ex. (left most is top of stack)
    push(1)
    [], [1]
    push(2)
    [1] [2,1]

if we want to pop, we'd want to get 1, 
    since that was the first in, so it's first out
    pop from the 1st stack,

    TRY THIS WITH A LONGER INPUT OUTPUT COMBO

    push(1)
    push(2)
    push(3)
    pop() # expect 1
    pop() # expect 2

    L is top of stack
    Stack1: [], Stack2: []
    push(1)
    Stack1: [1], Stack2: []
    push(2)
    Stack1: [2,1], Stack2: [1]
    push(3)
    Stack1: [3,2,1], Stack2: [2,1]
    pop()
    we want to retrieve 1, we can't.


ALT APPROACH:
- when we push, push to stack1
- when we pop, we'll transfer all of the stack onto stack2 in reverse order.
    then pop the top most element
    succeeding pops will be constant time
- when we push again, to preserve the order, we'll have to put the stack in reverse again

dry run:
    push(1)
    push(2)
    push(3)
    push(4)
    push(5)
    pop() # expect 1
    pop() # expect 2
    push(6)

    stack1: [], stack2: []
    push(1)
    stack1: [1], stack2: []
    push(2)
    stack1: [2,1], stack2: []
    push(3)
    stack1: [3,2,1], stack2: []
    ...
    push(5)
    stack1: [5,4,3,2,1], stack2: []
    pop()
    - pop each element from stack1 and push it onto stack2
        stack1: [4,3,2,1], stack2: [5]
        stack1: [3,2,1], stack2: [4,5]
        ...
        stack1: [], stack2: [1,2,3,4,5]

    - now, pop the element from stack2
    return 1
        stack1: [], stack2: [2,3,4,5]
    pop()
    return 2
        stack1: [], stack2: [3,4,5]

    - when we push again, we'd have to reverse the stack again
    push(6)
        stack1: [3], stack2: [4,5]
        stack1: [4,3], stack2: [5]
        stack1: [5,4,3], stack2: []
    - then push onto stack1
        stack1: [6,5,4,3], stack2: []

This approach gives us an "amortized" O(1) approach for each operation
    Although alternating between push and pop will take O(N),
    consecutive pushes and consecutive pops will give us O(1)
    obviously, peek and empty will be O(1) still.
'''
from collections import deque

class MyQueue:

    def __init__(self):
        self.is_pop = False
        self.pop_stack = deque()
        self.push_stack = deque()
        return

    def push(self, x: int) -> None:
        if not self.is_pop:
        # ie. we're in push mode
            self.push_stack.append(x)
        else:
        # ie. we're in pop mode
        # need to reverse the stack from pop_stack to push_stack
            while self.pop_stack:
                top_element = self.pop_stack.pop()
                self.push_stack.append(top_element)
            
            self.push_stack.append(x)
            # set to push mode
            self.is_pop = False

        return

    def pop(self) -> int:
        if self.is_pop:
        # ie. we're in pop mode
            return self.pop_stack.pop()
        else:
        # ie. we're in push mode
        # need to reverse the stack from push_stack to pop_stack
            while self.push_stack:
                top_element = self.push_stack.pop()
                self.pop_stack.append(top_element)
        
            # set to pop mode
            self.is_pop = True

        return self.pop_stack.pop()

    def peek(self) -> int:
        if self.is_pop:
            return self.pop_stack[-1]
        else:
            return self.push_stack[0]

    def empty(self) -> bool:
        if self.is_pop:
            return not self.pop_stack
        else:
            return not self.push_stack


'''
TEST CASE ANALYSIS:
["MyQueue","push","push","pop","push","push","pop","peek"]
[[],[1],[2],[],[3],[4],[],[]]

is_pop=False, pop_stack=[], push_stack=[]
push(1)
    is_pop=False, pop_stack=[], push_stack=[1]
push(2)
    is_pop=False, pop_stack=[], push_stack=[2,1]
pop() #expect 1
    is_pop=True, pop_stack=[2], push_stack=[]
push(3)
    is_pop=False, pop_stack=[], push_stack=[3,2]
push(4)
    is_pop=False, pop_stack=[], push_stack=[4,3,2]
pop() #expect 2
    is_pop=True, pop_stack=[3,4], push_stack=[]
peek() #expect 3
    is_pop=True, pop_stack=[3,4], push_stack=[]

'''


'''
PEEK ERROR:
its the fact that im using lists as stacks

'''