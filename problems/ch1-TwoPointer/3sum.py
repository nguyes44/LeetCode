'''
problem:
given an integer array nums, 
return ALL UNIQUE triplets
    ie. nums[i], nums[j], nums[k] where i !=j,k vice versa
such that nums[i] + nums[j] + nums[k] == 0

The order of output does not matter

--------------------------------------------------
sample input/output:
nums=[-1,0,1,2,-1,-4]
output:
[
    [-1,-1,2],
    [-1,0,1]
]
expl:
- all of these unique triplets sum to 0

nums=[0,1,1]
output:
[]
-The only possible triplet does not sum to 0

nums=[0,0,0]
output:
[
    [0,0,0]
]
- The only possible triplet sums to 0

custom input/output:
input:
[-1, -1, -1]
output:
[]
-All negative triplets cannot sum to 0

input:
[1,1,1]
output:
-All positive triplets cannot sum to 0

--------------------------------------------------
naive approach
- we'd need 3 pointers total, i,j,k
- can we iterate i, and use the two pointer approach with j and k?
    ie. have a sorted array
    pointers j,k at each end
    skip if any pointer indexes match (since we need unique indexes)
    check if the triplet sums to 0
    if sum == 0
        append to return array
    if sum < 0
        we need a greater value, move j to right
    if sum > 0
        need a smaller value, move k to left
        
TODO:
- how to ensure that our triplet is unique?
    ex. if we have [0,-1,-1] in our array, 
    we'll write [-1,0,-1], but that's not unique.

    - there might be a way to ignore triplets we've already checked

- consider the map approach;
    iterate i, j, but for k, we know the exact number we need to complete the sum
    check a map to see if the complement exists.
    O(N^2) approach me thinks, even if you avoid duplicates when iterating i,j

ex. 
nums=[-1,0,1,2,-1,-4], output:{ [-1,-1,2], [-1,0,1] }
nums.sort()
nums=[-4,-1,-1,0,1,2]

1st i iteration:
i=0, j=0, k=5
    -move j right

i=0,j=1,k=5
    -sum=-4+-1+2= -3
    => move j right for a larger num
i=0,j=2,k=5
    sum= -4,-1,2
    => move j right
i=0,j=3,k=5
    sum= -4, 0, 2 = -2
    move j right
i=0,j=4,k=5
    sum= -4,1,2= -1
    move j right
i=0,j=5,k=5
    not in while loop, since j not < k

2nd i iteration
- look at how we can determine if we're at an already checked triplet
- verify the current algorithm
i=1, j=0, k=5
    - we know that we've checked the triplet 0,1,5 already before
    - im thinking its bc j<i, so initialize j=i+1?
i=1, j=2, k=5
    sum= -1, -1, 2
    => add to list!
    now what? we need to continue checking triplets, but we can either
    move j right, or move k left
    dont think it matters, move j right
i=1, j=3, k=5
    sum= -1,0,2 =1
    => move k left
i=1, j=3, k=4
    sum= -1, 0, 1
    => add to list! 
    move j right
i=1, j=4, k=4
    done

3rd i iteration
i=2, j=0, k=5
    checked before
i=2, j=1, k=5
    checked before
i=2, j=3, k=5
    not yet

we've found all the correct triplets

--------------------------------------------------


'''

from typing import List

# CORRECT IMPLEMENTATION
def threeSum(self, nums: List[int]) -> List[List[int]]:
    triplets = []
    nums.sort()

    for i in range(0, len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        j=i+1
        k=len(nums)-1

        while j<k:

            sum = nums[i] + nums[j] + nums[k]

            if sum == 0:
                triplet = [nums[i], nums[j], nums[k]]
                triplets.append(triplet)
                j+=1
                while nums[j] == nums[j-1] and j<k:
                    j+=1
            elif sum < 0:
                j+=1
            elif sum > 0:
                k-=1
                
    return triplets

# MAP SPEEDUP IMPLEMENTATION
def threeSum(self, nums: List[int]) -> List[List[int]]:
    
    triplets = set()
    nums_map = {} # will hold {num_value: index}

    for i in range(0, len(nums)):
        nums_map[nums[i]] = i

    for j in range(0, len(nums)):

        for k in range(j+1, len(nums)):

            complement = -(nums[j] + nums[k])

            if complement in nums_map and nums_map[complement] != j and nums_map[complement] != k:
                triplet = [nums[j], nums[k], complement]
                triplet_tuple = tuple(sorted(triplet))
                triplets.add(triplet_tuple)

    triplets_list = [list(tt) for tt in triplets]

    return triplets_list


# MAP SPEEDUP IMPLEMENTATION, CHECKING 0 TUPLES
def threeSum(self, nums: List[int]) -> List[List[int]]:
    
    triplets = set()
    nums_map = {} # will hold {num_value: index}

    for i in range(0, len(nums)):
        nums_map[nums[i]] = i

    for j in range(0, len(nums)):

        for k in range(j+1, len(nums)):
            
            complement = -(nums[j] + nums[k])

            if complement in nums_map and nums_map[complement] != j and nums_map[complement] != k:
                triplet = [nums[j], nums[k], complement]
                triplet_tuple = tuple(sorted(triplet))
                triplets.add(triplet_tuple)
                continue

    triplets_list = [list(tt) for tt in triplets]

    return triplets_list



'''
FAILED TEST CASE:
nums=[-1,0,1,2,-1,-4]
exp. output:{ [-1,-1,2], [-1,0,1] }
- we get an extra [-1, 0, 1]
    since there is a duplicate -1
    therefore we need to check before inserting that our value is unique

can we just use a map?
the problem is that if there exists -1, 0, 1,
then 0, -1, 1 would still go through

replicate this scenario:
triplets = {[-1, 0, 1]}
current triplet = [0,-1,1]

what if i held a map triplets = {1st value: 2nd value}
ie. triplets = {-1: 0, 0: -1, 1:-1}

first, check if there exists a key match for nums[i]
ie. if triplets[0]
yes, there is a 0 key

now, check if there is a match for the second or third value
ie. if triplets[-1]
    complement_1 = 1
    complement_2 = 

would triplets clash?
    verify complements
    but then what if two triplets begin with -1?
    we would overwrite?

can i just use a set of tuples?


--------------------------------------------
FAILED TEST CASE:
all 0s, hella entries

- i think we have to use the search speedup map method
OR we can put a bandaid on the problem, and just check if we're all 0s

--------------------------------------------
SOLUTION:
- eliminate duplicates by first sorting the input array
    take advantage of the fact that the first pointer will be next to its duplicates
    therefore, if the previous value was the same, skip it.


'''