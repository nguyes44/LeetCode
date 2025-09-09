'''
initial solution using division:
- compute the whole array's product
- iterate again, for each i, append product/nums[i] to answer
    this would give us the product of the whole array,
    excluding nums[i]

------------------------------------
prefix/postfix sol:
- precompute the prefix and postfix of each i
prefix[i] is the product of all entries before and including i
postfix[i] starts from the right, goes to left

ex. nums=[1,2,3,4]

prefix = [1,2,6,24]
postfix = [24,24,12,4]

prefix[0] = 1
prefix[1] = 1*2
prefix[2] = 1*2*3
..

to get answer[0] for example,
value=1
we'd want the prefix (default 1)
    prefix[i-1] not valid, so default 1
multiplied by postfix (24)
    postfix[i+1] = 24
=> 1*24

the problem with this solution is that
we have O(2N) memory.

------------------------------------
optimal solution:
- iterate over nums to compute prefixes (inclusive)
    store the result in answer[i+1]
- iterate over nums R->L this time to compute postfixes
    multiply this result against answer[end-1-i]

    -1 since we ignore the right/left-most of answer,
    similar to how we did in first pass w/ i+1
'''

from typing import List

def productExceptSelf(self, nums: List[int]) -> List[int]:
    answer = []

    for i in range(len(nums)):
        answer.append(1)

    # first pass, we compute prefixes and write to answer
    prefix = 1
    for j in range(len(nums)):
        prefix = prefix * nums[j]

        if j+1 <= len(nums)-1:
        # ie. if the next index is in range
            answer[j+1] = prefix

    # second pass, compute postfixes and multiply with answer
    postfix = 1
    for k in range(len(nums)-1, 0, -1):
        postfix = postfix * nums[k]

        if k-1 >= 0:
            answer[k-1] = answer[k-1] * postfix
    
    return answer