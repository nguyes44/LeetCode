'''
problem:
given an array nums w/ 
n objects coloured red, white, or blue.

Sort them in-place so that 
objects of the same colour are adjacent
with the colours in the order red, white, and blue

Use 0, 1, and 2 to be red, white, blue respectively

Don't use Python's sort function.

--------------------------------------
input/output:
nums = [2,0,2,1,1,0]
output = [0,0,1,1,2,2]

nums = [2,0,1]
output = [0,1,2]

custom input/output:
nums = []
output = []

--------------------------------------
pseudocode:
- can't I just implement any in-place sorting algorithm?
would result in O(NlogN)

- instead, can I just scan 3 times to swap 0s, then swap 1s, etc?
would result in O(3N) => O(N)

- keep track of an index to swap at, cur.
- on a pass (ex. finding 0s)
    if i's value is 0 
    AND the values are different
    AND i != c (ie. we can actually swap)
        swap with index c
        increment c

'''

from typing import List

def sortColors(self, nums: List[int]) -> None:
    if len(nums) == 0 or len(nums) == 1:
        return

    swap_index = 0
    # going to perform each pass to find 0, 1, 2s
    for val in range(2):
        for i in range(swap_index, len(nums)):
            if nums[i] == val and nums[i] != nums[swap_index] and i != swap_index:
                nums[i], nums[swap_index] = nums[swap_index], nums[i]
                swap_index += 1
        
        # after a pass to find a 0, 
        # need to move swap_index to the right-most 0
        while nums[swap_index] == val:
            swap_index += 1
            if swap_index >= len(nums) - 1:
                break

    return

'''
failed test case:
nums = [0, 1]
expected: [0, 1]
actual: [1, 0]

failed test case:
nums = [0,0]
out of range


'''