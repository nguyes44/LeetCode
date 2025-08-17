'''
Given an array of integers "nums" and an integer "target", 
return the indicies of the two numbers such that they add up to "target"

You may assume that each input would have exactly one solution, 
and you can't use the same element twice

Can return the answer in any order.

Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0,1] since 2 and 7 add up to 9

input: nums = [3, 2, 4], target = 6
output: [1, 2]

input: [3, 3], target = 6
output: [0, 1]

custom input: [4, 2, 0, 6, 9], target = 11
output: [1, 4]

3. We know that the approach is two pointer.
How do we apply it? Recall that the two pointer approach breaks down to 2 approaches,
    1. opposite ends, converge
    2. different paces
I think we need to use convergence


4. Pseudocode:
sort the array into a map, which keeps the original index as the key, and the value
initialize the indicies at the ends of the map.
begin iterating from i=0 to end (since we know its O(N)) 
    check if the pair's values sum to target.
    if so, return their keys


The brute force approach IS to iterate O(N^2)

Can we sort it first?
If we sort it, then we have the exact same problem as the example in one pointer in each end.

Sorting via the best sorting algorithm (idk) would give us O(N * logN)
We also have to turn it into a list again, which is O(N)
Then, we know our approach is O(N)
so our total runtime is O(3N*logN)

The current space complexity is derived from:
O(N) due to the map storing both original indicies and values
O(N) to for the new "items" list
Total: O(2N) -> O(N)

To improve this, we can instead transform the list directly to the list of tuples, 
which avoids an intermediate map
'''
from typing import List


def map_original_indices_to_sorted_values(arr):
    sorted_with_indices = sorted(enumerate(arr), key=lambda x: x[1])
    return {original_index: value for original_index, value in sorted_with_indices}

def two_sum(nums: List[int], target: int):
    pointer_1 = 0
    pointer_2 = len(nums) - 1

    sorted_map = map_original_indices_to_sorted_values(nums)
    items = list(sorted_map.items())

    for i in range(len(items)):
        # check if the pair's values sum to the target
        sum = items[pointer_1][1] + items[pointer_2][1]

        if sum == target:
            return [items[pointer_1][0], items[pointer_2][0]]
        elif sum < target:
            # ie. sum too small, we need a larger number
            pointer_1+=1
        else:
            # ie. sum too big, need smaller number
            pointer_2-=1
        
    # if we reach here, we didn't get anything
    return [0,0]

def main():
    nums1 = [2, 7, 11, 15]
    target1 = 9

    nums2 = [4, 2, 0, 6, 9]
    target2 = 11

    print(two_sum(nums1, target1))
    print(two_sum(nums2, target2))


    return

main()

'''
The alternative approach that doesnt use two pointers is:
-initialize an (unsorted) map storing the element as key, index as value
-traverse the input array
-for each element in the array, search for the complement using the formula
    target - first_num = complement
-we can lookup the complement in the map at O(1) if it exists
-if it exists, we can return the index of the complement and first_num's index

Time complexity:
-We need to initialize the map by traversing original array, so O(N)
-Then, we iterate over the array once to find the complement, O(N)
=> O(2N), or O(N)

Space complexity:
-The additional map will be O(N)

    
'''