'''
problem:
Given an unsorted integer array nums,
return the smallest, positive integer that is not present in nums

Implement in O(n) time and O(1) space

Input: [1, 2, 0]
Output: 3
Expl: the positive numbers that exist are 1, 2. 
The smallest positive that's not present is 3
(missing can be at the end)

Input: [3, 4, -1, 1]
Output: 2
Expl: the positive numbers are 1, 3, 4.
The smallest one that is missing is 2
(missing can be within the range)

Input: [7, 8, 9, 11, 12]
Output: 1
Expl: the positive numbers are 7,8,9,11,12
The smallest missing one is 1
(missing can be at the end)

DSA:
Use Cyclic Sort, because we're:
- dealing with an array
- required to find a missing
- required to implement in O(N) time, O(1) space

pseudocode:
iterate to find the range of min-max positive integers
    if the min-1 >= 1
    return min-1
# at this point, we know the min is either within the range, or at the right end

iterate through the array to cyclic sort it.
how do we find the correct indexes of these numbers?
- ignore the non-positive numbers (incl. 0)
- the first index should be the min
- the second index should be the min + 1
...

WALKING THROUGH INPUT:
ex. [3, 4, -1, 1]
1. i=0, val = 3, min = 1, max = 4
    using the min and max, we predict that val=3 should belong to index: val-1=2
    [-1, 4, 3, 1]

2. i=0, val=-1,
    val is non-positive, so we ignore.
    Increment i
    [-1, 4, 3, 1]

3. i=1, val=4
    using the min and max, we predict that val should belong to index: val-1=3
    [-1, 1, 3, 4]
4. i=1, val=1
    using the min and max, we predict that val should belong to val-1=0
    [1, -1, 3, 4]
5. i=1, val=-1
    non-positive, ignore
    Increment i
    [1, -1, 3, 4]
6. i=2, val=3
    swap with index val-1=2
    can't swap, so increment i
    [1, -1, 3, 4]
7. i=3, val=4
    swap with index val-1=3
    can't swap, so increment i

this is now cyclic sorted
now, iterate to find the smallest, positive missing number
initialize expected_number := min
1. i=0, val=1
    this is our min, so we're okay
    increment exp. num. & i
2. i=1, val=-1
    ignore non-positive numbers
    increment i
3. i=2, val=3
    exp. num = 2, while the val is 3.
    => 2 is the smallest positive missing number.


how do we scale the cyclic sort with super large numbers?
ex. [300, 400, -1, 1]

1. i=0, val=300, min=1, max=400
    how do we predict which index to put the val=300?

**WHAT CAN WE DEDUCE ABOUT THE RETURN VALUE?

- the key is to also ignore values that are larger than len(nums)
    for example, if len(nums)=4, then we know the smallest, missing positive number is in
    [1,2,3,4,5]
    anything outside of this range can be ignored

ex. [300, 400, -1, 1]
1. i=0, min=1, max=400, val=300, len(nums)=4, range=[1,2,3,4,5]
    should we swap this value?
    it is outside the range, (ie. range_max=5)
    so no.
    increment i
2. same
3. value is negative, ignore.
This is now cyclic sorted.

Now, iterate to find the smallest, positive, missing number
expected_num := min (ie. 1)
1. i=0, val=300
    outside of range, ignore
2. i=1, val=400
    outside of range, ignore
3. i=2, val=-1
    negative, ignore
4. expected_num == val,
    increment expected_num

return expected_num

- i dont think i need to use max & min anymore.
GENERALIZE THE CYCLIC SORT ALGORITHM to ignore numbers outside of the range,
since they don't affect the return value
ex. [3, 4, -1, 1]

init:
len(nums)=4,
min, max = 1, 4 (since O(1) space)
=> our range is [1,2,3,4]
if we exceed len(nums), then return len(nums)+1

1. i=0, val=3
    use our range to determine where the value goes.
    correct_index=val-min
    =3-1
    =index 2
    => swap with index 2
    [-1, 4, 3, 1]
2. i=0, val=-1
    ignore since negative.
    iterate i
3. i=1, val=4
    val-min
    =4-1
    =index 3
    => [-1, 1, 3, 4]
4. i=1, val=1
    val-min
    =1-1
    =index 0
    => [1, -1, 3, 4]
5. i=1, val=-1
    ignore negative, 
    iterate i
6. i=2, val=3
    val-min
    =3-1
    =index 2,
    val == nums[correct_index],
    don't swap.
    iterate i
7. i=3, val=4
    val-min
    =4-1
    =3
    val == nums[correct_index]
    don't swap,
    iterate i

we end up with the array:
[1, -1, 3, 4]

finally, iterate through it with expected numbers, starting at min
    if we find a positive, within range number that is not our expected number,
    return that number.
'''

from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    # this represents the range which our return value could fall in
    min = 1
    max = len(nums)

    # CYCLIC SORT
    i = 0
    while i < len(nums):
        # ignore if non-positive (incl. 0) or outside of range
        if nums[i] > 0 and nums[i] <= max:
            correct_index = nums[i]-min

            # ie. if the value is already at its correct index
            if correct_index == i or nums[i] == nums[correct_index]:
                i+=1
            else:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i+=1
        
    # DETERMINE MISSING NUM
    expected_num = min
    for num in nums:
        if num != expected_num:
            return expected_num
        else:
            expected_num+=1

    return expected_num

def main():
    print(firstMissingPositive([3, 4, -1, 1]))

main()