'''
problem:
climbing a staircase.
n steps to reach the top.
at each step, you can take either 1 or 2 steps.

how many distinct ways can you climb to the top?

-------------------------------------------------
pseudocode:
- the main problem is:
    "at step 0, how many ways can i get to step n?"
- at this point, we can make 2 choices:
    1 or 2 steps
- with this depiction, we can create a decision tree:
    each node's value is what step we're at.
    each node branches off by taking either 1 or 2 steps
- each node is also a subproblem.
    ie. "at step 3, how many ways can i get to step n?"
- we observe that subproblem X depends on result of subproblem X+1 and X+2
    ex. at step 3, we can either take 1 or 2 steps,
    which leads us to being at either step 4 or 5.
    The number of ways from step 3 to end is from adding number of ways from step 4 and 5.

- use "bottom-up DP"
    ie. start at the bottom of the decision tree, at step n
- there is only 1 way to get to end, and we're there.
- move to next subproblem, step 4 (ie. n-1)
- at step n-1, we can only take 1 step.
    => only 1 way
- at step 3, (ie. n-2), like stated before, we get the result by adding previous 2.
    => 1+1 = 2
- continue until we solve for step 0, the beginning.

'''

def climbStairs(self, n: int) -> int:
    # represents the decision to take 1 or 2 steps
    one_step = 1
    two_step = 1

    if n == 2:
        return one_step + two_step
    elif n == 1:
        return one_step

    step_count = n-2
    # keep computing until we compute for step 0
    while step_count >= 0:
        subproblem_result = one_step + two_step
        
        # shift each variable "one to left of DP array"
        two_step = one_step
        one_step = subproblem_result

        # move to the next subproblem
        step_count -= 1

    return subproblem_result

'''
time complexity:
- since you only need to compute n-2 subproblems,
O(N)

space complexity:
we hold 3 variables no matter n size
=> O(1)
'''