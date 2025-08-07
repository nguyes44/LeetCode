'''
Problem:
Given an array of intervals, where intervals[i] = [start_i, end_i],
merge all overlapping intervals, and
return an array of the non-overlapping intervals 
that cover all the intervals in the input.

ex. input/output:
input:
[1,3], [2,6], [8,10], [15,18]
output:
[1,6], [8,10], [15, 18]
This is because [1,3] and [2,6] overlapped, and thus was combined to [1,6]

input:
[1, 4], [4, 5]
output:
[1,5]
This is because 4 and 4 are considered overlapping

edge case identification:
-input []
should output []

DSA:
we'll use merge intervals, since the approach is designed to merge intervals 
that have overlap.

pseudocode:
-initialize a final_list
-sort the intervals based on starting time.
-insert the first interval into final_list
-iterate over the intervals starting from the second interval
    -compare the end time of the first interval to the start time of the second interval
        (if 1st end time >= 2nd start time, merge interval)
        merge interval by updating the 1st interval's end time to the 2nd's end time

return the final_list 

'''
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        # sort the intervals based on start times
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        merged.append(intervals[0])
        for i in range(1, len(intervals)):
            if merged[-1][1] >= intervals[i][0]:
            # ie. latest item's end time vs. ith interval's start time
            # need to check if updating is also valid too
            # not valid example:
            # [1, 4], [2, 3]
            # we'd merge this yes, but not by overwriting merged[-1][1] with the ith interval's end value
            # we'd simplify into [1, 4]
            # therefore, we need to check HOW to merge if we've determined merging is necessary 
                if merged[-1][1] >= intervals[i][1]:
                    pass
                else:
                    merged[-1][1] = intervals[i][1]
                    # update merged[-1]'s end time
            else:
                merged.append(intervals[i])
        
        return merged
    

'''
LEARNING NOTES:
.sort performs sorting "in-place," 
which means it modifies the list directly

the key is what to sort based on.
here, we want to sort based on the start value of each interval
ie. x[0]

lambda x: x[0]
this is an anonymous function that takes one argument, x,
then returns x's first item

the key parameter in .sort()
key is a function.
for each item, Python computes func(item)
then, the items are sorted based on each result of those calls
'''

'''
For next time:
-improve on edge case creation, look at values inside the values (if possible)
'''

'''
TIME/SPACE COMPLEXITY ANALYSIS:
Time:
-first, we sort. O(N*logN), where N is the number of intervals
-then, we iterate over the intervals once, O(N)
O(N + NlogN)
=> O(N*logN)

Space:
-Python built-in sorting is O(N) space; uses Timsort
-then, we create the "merged" array, which will contain all N intervals
=> O(2N)
'''

'''
IMPROVEMENTS:
-this algorithm is the preferred approach to solving the merge intervals problem, 
i dont think there's a better solution
'''