'''
problem:
design a stack that supports 
    -push, 
    -pop, 
    -top, 
    -retrieving the min element in O(1)

-----------------------------------------------
INPUT/OUTPUT:
push(-2)
push(0)
push(-3)
getMin() # return -3
pop() # REMOVE -3
push(-7)
push(-5)
top() # return 0
getMin() # return -2


CUSTOM INPUT/OUTPUT:
push(-3)
push(-4)
push(1)
getMin() # return -4
pop() # REMOVE 1
top() # return -4
getMin() # return -4

-----------------------------------------------
APPROACH:
- I will use Python's implementation of a stack, deque.
- It's easy to keep track of the most recent min
- The problem is how do we get the next min?

ATTEMPT:
- use a stack to keep track of values normally
- use another stack to keep track of most recent mins
'''

from collections import deque

class MinStack:

    def __init__(self):
        self.normal_stack = deque()
        self.min_stack = deque()
        self.min = float('inf')
        return

    def push(self, val: int) -> None:
        if val <= self.min or not self.normal_stack:
            self.min = val
            self.min_stack.append(self.min)

        self.normal_stack.append(val)
        return

    def pop(self) -> None:
        if self.normal_stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

            if self.min_stack:
                self.min = self.min_stack[-1]

        self.normal_stack.pop()
        return

    def top(self) -> int:
        return self.normal_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
    

'''
ERROR:
push(0)
push(1)
push(0)
- Technically, 0 and then 0 again should be pushed onto the min stack. Whoops

------------------------
push(6) inst. 1
push(6) inst. 2
push(7)
top() # return 7
pop() # REMOVE 7
getMin() # return 6 inst. 2
pop() # REMOVE 6 inst. 2
getMin() # return 6 inst. 1
pop() # REMOVE 6 inst. 1
push(7)
top() # return 7
getMin() # return 7
push(-8)
top() # return -8
getMin() # return -8
pop # REMOVE -8
getMin() # return 7

- On push(), I wasn't adding to the min_stack when normal_stack was empty, 
    even though the new element should be a min since there's nothing on the stack

------------------------

,"getMin","getMin","pop","getMin","push","push","pop","push","getMin","getMin","push","getMin","getMin","push","getMin","getMin","getMin","push","getMin","pop","top","push","top","push","getMin","getMin","push","pop","getMin","getMin","pop","pop","getMin","push","getMin","getMin","push","getMin","top","getMin","push","getMin","push","top","getMin","push","getMin","top","getMin","push","getMin","getMin","push","pop","push","push","getMin","push","push","push","top","getMin","push","getMin","push","push","push","getMin","push","push","push","pop","push","getMin","top","getMin","getMin","push","top","push","push","top","push","getMin","push","top","getMin","getMin","getMin","getMin","getMin","push","getMin","push","push","getMin","getMin","getMin","top","getMin","push","pop","getMin","getMin","push","getMin","getMin","getMin","getMin","push","top","top","push","push","push","top","top","push","getMin","push","push","push","getMin","getMin","push","push","push","push","getMin","getMin","getMin","push","top","pop","getMin","push","top","pop","push","getMin","pop","getMin","pop","getMin","push","top","push","getMin","getMin","top","pop","top","getMin","getMin","push","push","push","pop","push","getMin","getMin","push","push","push","top","getMin","top","getMin","getMin","top","top","pop","pop","getMin","getMin","push","getMin","push","getMin","push","push","push","getMin","pop","pop","push","pop","top","push","top","top","pop","top","push","push","top","top","getMin","getMin","getMin","push","getMin","getMin","push","getMin","pop","top","push","push","push","push","push","getMin","getMin","push","getMin","getMin","getMin","push","getMin","getMin","getMin","top","getMin","getMin","push","top","getMin","push","getMin","push","getMin","getMin","getMin","push","pop","push","pop","push","top","getMin","getMin","push","getMin","getMin","getMin","push","push","push","getMin","push","top","push","getMin","push","top","getMin","getMin","getMin","pop","getMin","top","getMin","push","getMin","getMin","getMin","getMin","getMin","pop","getMin","getMin","push","getMin","pop","push","top","push","push","getMin","pop","pop","push","pop","getMin","push","push","getMin","getMin","pop","pop","pop","push","pop","push","push","push","push","getMin","top","getMin","getMin","getMin","top","push","getMin","push","push","getMin","pop","getMin","push","pop","pop","push","push","push","pop","getMin","getMin","pop","push","push","getMin","top","getMin","pop","push","push","push","getMin","getMin","push","push","push","getMin","pop","getMin","push","push","getMin","getMin","getMin","push","getMin","getMin","getMin","getMin","getMin","getMin","push","getMin","pop","getMin","getMin","push","pop","pop","pop","push","top","push","push","getMin","getMin","getMin","getMin","getMin","push","push","top","push","top","push","top","pop","push","getMin","push","push","getMin","getMin","getMin","getMin","pop","getMin","push","top","pop","push","getMin","push","push","push","push","pop","getMin","push","push","top","getMin","getMin","top","getMin","getMin","push","getMin","push","getMin","top","getMin","getMin","push","push","getMin","push","push","push","push","getMin","getMin","pop","push","top","push","pop","getMin","push","push","getMin","getMin","push","getMin","push","push","getMin","getMin","getMin","top","getMin","getMin","push","top","push","top","pop","push","push","getMin","push","pop","pop","push","getMin","push","getMin","getMin","getMin","top","top","pop","pop","pop","getMin","push","top","push","getMin","getMin","getMin","push","getMin","top","getMin","push","push","getMin","pop","getMin"]
,[],[],[],[],[-158],[82],[],[-176],[],[],[-90],[],[],[411],[],[],[],[-494],[],[],[],[155],[],[-370],[],[],[273],[],[],[],[],[],[],[173],[],[],[0],[],[],[],[-266],[],[-359],[],[],[189],[],[],[],[375],[],[],[-188],[],[-275],[-223],[],[294],[380],[-42],[],[],[33],[],[457],[422],[-352],[],[326],[-378],[231],[],[416],[],[],[],[],[277],[],[472],[205],[],[-443],[],[-5],[],[],[],[],[],[],[-312],[],[-249],[-209],[],[],[],[],[],[196],[],[],[],[-347],[],[],[],[],[400],[],[],[269],[434],[-213],[],[],[-58],[],[-353],[-426],[-335],[],[],[-188],[-388],[369],[319],[],[],[],[121],[],[],[],[155],[],[],[155],[],[],[],[],[],[495],[],[-53],[],[],[],[],[],[],[],[465],[162],[-334],[],[282],[],[],[432],[-418],[195],[],[],[],[],[],[],[],[],[],[],[],[374],[],[202],[],[181],[173],[-323],[],[],[],[-430],[],[],[346],[],[],[],[],[244],[-467],[],[],[],[],[],[279],[],[],[-30],[],[],[],[264],[-217],[-418],[12],[-439],[],[],[7],[],[],[],[-189],[],[],[],[],[],[],[303],[],[],[-297],[],[-21],[],[],[],[461],[],[-303],[],[-338],[],[],[],[-42],[],[],[],[85],[132],[57],[],[-17],[],[-10],[],[-500],[],[],[],[],[],[],[],[],[-7],[],[],[],[],[],[],[],[],[346],[],[],[16],[],[472],[-211],[],[],[],[-381],[],[],[214],[169],[],[],[],[],[],[33],[],[115],[-346],[-309],[130],[],[],[],[],[],[],[335],[],[-92],[-16],[],[],[],[-470],[],[],[250],[327],[144],[],[],[],[],[359],[138],[],[],[],[],[272],[-241],[-362],[],[],[-83],[195],[-208],[],[],[],[-500],[5],[],[],[],[284],[],[],[],[],[],[],[477],[],[],[],[],[30],[],[],[],[-269],[],[-413],[-323],[],[],[],[],[],[217],[-408],[],[-353],[],[-142],[],[],[-321],[],[-33],[382],[],[],[],[],[],[],[298],[],[],[495],[],[195],[-147],[-85],[195],[],[],[154],[-311],[],[],[],[],[],[],[-390],[],[323],[],[],[],[],[338],[263],[],[160],[148],[142],[427],[],[],[],[-153],[],[-384],[],[],[159],[419],[],[],[-385],[],[461],[-346],[],[],[],[],[],[],[343],[],[-269],[],[],[-401],[81],[],[130],[],[],[-428],[],[454],[],[],[],[],[],[],[],[],[],[59],[],[143],[],[],[],[-154],[],[],[],[114],[-346],[],[],[]]

STOP WHEN WE RETURN 29, IDENTIFY THE PROBLEM. WE NEED -251
at 14 calls (incl. init, so 13 real calls)
**verify if the output trace matches ours

push(395)
getMin() # return 395
top() # return 395
getMin() # return 395
push(276)               # NEW MIN
push(29)                # NEW MIN
getMin() # return 29
push(-482)              # NEW MIN
getMin() # return -482
pop() # REMOVE -482

push(-108)              # NEW MIN
push(-251)              # NEW MIN
getMin() # return -251
push(-439)              # NEW MIN
top() # return -439
push(370)
pop() # REMOVE 370
pop() # REMOVE -439
getMin() # return -251 # HERE IS THE PROBLEM


- I'm stupid. When I'm popping from both stacks, I'm not updating self.min to be the next min
'''