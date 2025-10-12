'''
problem:
Given a string s
containing characters '(', ')', '{', '}', '[', and ']'
determine if the input string is valid.

Valid if:
- open brackets must be closed by same type of brackets
- open brackets must be closed in the correct order
- every close bracket has an open bracket of the same type

-----------------------------------------
input/output:
s=()
true

s="()[]{}"
true

s = "(]"
false

s = "([])"
true

s = "([)]"
false

custom input/output:
s=(
false
s= ({}[])

-----------------------------------------
pseudocode:
- i think this is a stack problem.
- iterate over the string
- if we see an open bracket,
    push onto stack
- if we see a closed bracket,
    check if top of stack has corresponding open bracket
    if so, pop off stack
    if not, return false

reached the end of string.
    if top of stack == None,
        return true
    else
        return false

'''

def isValid(self, s: str) -> bool:
    stack = []

    for char in s:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)

        elif len(stack) != 0:

            if char == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False

            elif char == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False

            elif char == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False

        elif len(stack) == 0 and (char == ')' or char == ']' or char == '}'):
            return False
        
    if len(stack) == 0:
        return True
    else:
        return False
    
'''
time complexity:
- iterate over the string once
O(N)

space complexity:
- worst case, we have N open brackets
=> O(N)

'''