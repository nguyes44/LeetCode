'''
use bucket sort, O(N) time:
- scan the input array,
- count how many times each value occurs
for each value in bucket sort,
    write the value in the next X indicies,
    where X is the number of times it occurs

---------------------------------------------
single-pass sol:
- keep track of a left and right pointer
    left: responsible for putting 0s on left
    right: responsible for putting 1s on right

- whenever we run into a 0 value,
    we swap with left pointer, 
    increment left inwards
    increment i

- whenever we run into a 2 value,
    swap with right pointer
    increment right inwards
    DONT increment i, 
        this is because by swapping with right,
        we could introduce a 0 into the ith index

        vice versa is not true for left,
        bc left can only point to 0, or 1
        the i pointer already passed it,
        so any 2 would have been swapped w right

- when i > right, we're done
    bc any portion to the right 
    of the right pointer is already processed.
'''

from typing import List

def sortColors(self, nums: List[int]) -> None:
    if len(nums) == 0 or len(nums) == 1:
        return

    left = 0
    right = len(nums)-1
    i = 0

    while i <= right:
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            i += 1

        elif nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
        else:
            i += 1
    
    return
