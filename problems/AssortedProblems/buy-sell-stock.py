'''
problem:
Given: array prices, 
    where prices[i] is the price of a stock on day i

Maximize profit by:
- choosing a single day to buy one stock
- choosing a future day to sell that stock

------------------------------------------------------
input:
    prices = [7,1,5,3,6,4]
output: 5
expl: you buy on day 2, and sell on day 5

input:
    prices = [7,6,4,3,1]
output: 0
expl: you can't make profit on any day that you buy
(ie. prices is monotonically decreasing)

------------------------------------------------------
EDGE CASES:
input:
    prices = []
output:
    0, there is nothing to sell

input:
    prices = [1, 2]
output:
    1

input:
    prices = [1, 2, 3, 4, 5]
output:
    4, buy day 1, sell day 5

------------------------------------------------------
DSA:
Two pointer, since you're essentially finding a pair
with the largest difference whose indexes are not "across" each other
    ie. index i < index j

Brute force:
I'd start at index 0, and 
    iterate across the whole array to the right to find the lowest pair
I'd do the same for index 1, 2, etc.

------------------------------------------------------

pseudocode:
- initialize two pointers on each end; buying & selling
- compute the initial profit
- check to see if moving left or right is "more profitable"
'''

# INCORRECT OPTIMAL SOLUTION
# TWO POINTER ATTEMPT
from typing import List

def maxProfit(self, prices: List[int]) -> int:
    buying = 0
    selling = len(prices) - 1
    profit = prices[selling] - prices[buying]

    while buying < selling:
        if prices[selling] - prices[buying+1] >= profit:
            buying+=1
            profit = prices[selling] - prices[buying]

        elif prices[selling-1] - prices[buying] >= profit:
            selling -=1
            profit = prices[selling] - prices[buying]

        else:
            selling -= 1

    if profit <= 0:
        return 0

    return profit

'''
i have an infinite loop somehow
    its bc i didnt consider the case where it wasn't profitable to move at all

if its equal, we should move it as well. We can potentially see a better time in the future.

fails on [2,1,2,0,1]
output: 0
expected: 1

profit = -1
1. buying=0, selling=4
    profit from moving buying right is greater than current
    (0 > -1)
    move right
2. buying=1, selling=4
    we can't get to the correct solution, since we don't want to buy for greater
        ie. move buying's value right from 1->2
    and don't want to sell for cheaper
        ie. move selling's value left from 1->0
    however, the optimal solution is just past it
    we need to move selling just one more to the left

    Therefore, we shouldn't judge based on immediate profit.
    We should continue iterating selling to the left in search
        of a new max
    Same with buying, continue iterating in search of a new min
        
    How do we know when to stop?
    when the pointers meet




WHAT EDGE CASE DID I MISS
- the non-increasing ones (ie. [2,1,2,0,1])

[2,1,2,1,0,1,2]

1. b=0, s=6
    move b right
2. b=1, s=6
    move s left (else case, profit isnt changed)
3. b=1, s=5


we shouldnt even be moving s to the left at all, 
    the solution is 0, 2
'''


'''
NEW PSEUDOCODE:
iterate through the array once
keep track of the min that you've found thus far
for each day, ask "what if i sold today?"
    if you've just found a new min, selling would make no sense
'''

from typing import List

def maxProfit(self, prices: List[int]) -> int:
    min = float('inf')
    profit = 0

    for price in prices:

        if price < min:
            min = price

        if price - min > profit:
            profit = price - min

    return profit

'''
Time Complexity:
since we're iterating only once, it is O(N)

Space Complexity:
we're initializing 2 variables, so O(1)
-------------------------------------------------------------
'''