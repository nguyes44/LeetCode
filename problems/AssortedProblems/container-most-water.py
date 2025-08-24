'''
problem:
given - height; integer array of length n
There are n vertical lines whose heights are height[i]

Find two lines that, together with the x-axis form a container, 
    such that the container contains the most water

Return the max amount of water a container can store.

-----------------------------------------------
INPUT/OUTPUT:
input: [1,8,6,2,5,4,8,3,7]
output: 49
explan: the highest and widest walls of the container are 8, 7
    this gives us a water amt of length * height
    length = index j - index i
        = 8-1
        = 7
    height = min(height[i], height[j])
        = min(8, 7)
        = 7

input: [1, 1]
output: 1, since 1*1

custom input/output:
input: [1, 0]
output: 0

input: [2, 2,... x20, 20, 20, 2, ... x20, 2] 60 times
here, if we just use the heights, we'd come to the result of 20*1
but we need to identify that the correct approach is going wide. 
    2*60 = 120

-----------------------------------------------
FIRST ATTEMPT PSEUDOCODE:
- our goal is to find the largest values that are also furthest apart
- begin with pointers at each end of the height array
    left_pointer = 0
    right_pointer = len(height)-1
- hold a "max_water" value = length * height
    length = abs(right_pointer - left_pointer)
    height = min(height[left_pointer], height[right_pointer])

- try every combination
    for left_pointer in range(0, len(height)-1): # ie. each left pointer value
        for right_pointer in range(len(height)-1, 0, -1): # ie. each right pointer value
            compute water
            if water > max_water:
                max_water = water

    return max_water

'''

from typing import List

def maxArea(height: List[int]) -> int:
    max_water = float('-inf')
    max_length = len(height)-1
    max_height = height[0]

    # start by assuming horizontal, 
    # since we don't know max_height yet
    is_horizontal = True
    first_pass = True

    for i in range(0, len(height)):

        if height[i]==0:
            # we can't use 0 in any pair
            continue

        # don't go past i,
        # since we've checked those pairs already
        for j in range(len(height)-1, i, -1):

            if height[j]==0:
                continue

            if first_pass and height[j] > max_height:
                max_height = height[j]

            water_length = j - i
            water_height = min(height[i], height[j])

            # after our first pass, 
            # we'll know 100% if the solution is vertical or horizontal
            if not first_pass and is_horizontal:
                # dismiss this iteration if its water is vertical,
                # while we know the solution is horizontal
                if water_height > max_length:
                    print(i,j, "being skipped A")
                    continue

            elif not first_pass and not is_horizontal:
                if water_length > max_height:
                    print(i,j, "being skipped B")
                    continue

            # now, try to compute the water amt
            water_amt = water_length * water_height
            print(i,j)
            print("water length:", water_length)
            print("water height:", water_height)
            print("water amt:", water_amt)

            if water_amt > max_water:
                max_water = water_amt

        first_pass = False
        if max_height > max_length and not first_pass:
            is_horizontal = False

    if max_water == float('-inf'):
        return 0

    return max_water

#### IMPLEMENTATION 2

def maxArea(height: List[int]) -> int:
    max_water = float('-inf')
    max_length = len(height)-1
    max_height = height[0]

    is_horizontal = True

    # first pass to find max_height
    for i in range(0, len(height)):
        if height[i] > max_height:
            max_height = height[i]
    
    # second pass, 
    # we know whether our solution is vertical or horizontal
    # constrain one of the points


    return

def main():
    maxArea([1,2,3,1000,9])
    return

main()

'''
Time Complexity:
- since we move right pointer N times for each N items, it is N*N = O(N^2)

Space Complexity:
- we initialize max_water, left_pointer, right_pointer, and water_length/height/amt.
=> O(1)

-----------------------------------------------
THOUGHTS TO OPTIMIZE:
Q: how can we reduce the number of iterations?
ie. how do we know to stop one of the pointers from moving?

the solution is either:
    1. greater horizontal lengthed rectangle (or square)
        - when max_length > max_height
    2. greater vertical lengthed rectangle (or square)
        - when max_length < max_height
    3. anything
        - when max_length = max_height
    4. none 
        ex. [0,5,0]
        ex. [0,1]
        ex. [0,0,0,1,0]

ex. max_length=9
    max_height=8

can we have an input that would result in a vertical lengthed rectangle?
ex. [8,8,6,2,5,4,8,3,8], keep max_length and max_height same
    no matter what, we'd have a horizontal solution


-assuming we know the max_height and max_length, 
    we can ignore pairs that violate this solution property
    ex. if max_length > max_height, we know the solution is horizontally lengthed (or square)
    ignore the pair if height > length 


ONE STEP FURTHER:
- can we say that our solution must have a length >= max_height? and vice versa
ex. [8,8,6,2,5,4,8,3,8], max_height=8, max_length=9

if length < max_height here, then we have a vertically oriented rectangle, 
    which is NOT what our assumption provides

-----------------------------------------------
FURTHER OPTIMIZE:
- after our first pass, we know whether our solution is vertical or horizontal
    let's say its vertical
    shouldn't we constrain one of our pointers to the max_height, then check for pairs?
    is there ever a vertical solution that doesn't use the max_height?
    can we just find the next greatest value?
disprove:
    [999,999,3,1000,9, 0, 0, 999]
    max_height=1000
    max_length=4

constrain 1000, the next greatest value is 999 on the left
but it can also be on the right.
We'd just have to do one more pass to find the largest water_amt

What to do if the solution is horizontal?


-----------------------------------------------
FAILED TEST CASE:
[8,7,2,1]
-the solution is
max_length=3
max_height=8
=> vertical

8, 7 => 7*1=7
----------------
[1,2,3,1000,9]
max_height=1000
max_length=4
-we'd expect the solution to be vertical

-----------------------------------------------
SOLUTION:
two pointer; move the pointer that currently has the least height, since that is the restraining value
'''
# WORKING SOL
def maxArea(self, height: List[int]) -> int:
    max_water = float('-inf')
    left_pointer = 0
    right_pointer = len(height)-1
    water_amt=0
    water_height=0
    water_length=0

    while left_pointer < right_pointer:
        water_height=min(height[left_pointer], height[right_pointer])
        water_length=right_pointer-left_pointer
        water_amt=water_height*water_length

        if water_amt > max_water:
            max_water=water_amt

        if height[left_pointer] <= height[right_pointer]:
            left_pointer+=1
        elif height[right_pointer] <= height[left_pointer]:
            right_pointer-=1
        
    return max_water