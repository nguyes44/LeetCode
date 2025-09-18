'''
Algorithm:
1. Choose a "pivot" which will be 
swapped with the right most element

2. left and right pointers will iterate;
    left - first element less than pivot
    right - first element greater than or equal to pivot
    stop when left index > right index
    swap left index w/ pivot
    now, pivot is in correct spot.
        - left items are < pivot
        - right items are >= pivot

3. call recursively on subarrays

base case - single item; already sorted


pivot choosing: 
    median of 3; good vs. worst cases

worst case:
- choosing a pivot that is largest/smallest
    leads to extremely unbalanced partitions,
    => recursive depth is O(n)
- since each partition is O(n),
total time is O(n*n)

average case is O(nlogn) because:
- recursive depth (of balanced partitions)
~ O(logN)
- each layer of the recursion tree does O(N) total
O(N* log N)
'''
from typing import List

def quick_sort(arr: List, start: int, end: int):
    n = len(arr)

    # base case
    if (end-start)==1:
        return arr

    # choose a pivot; median
    pivot = int(n/2)

    left = start
    right = end

    # swap pivot with right most element
    arr[pivot], arr[right] = arr[right], arr[pivot]

    while left < right:
        # find the first left element that's greater than pivot
        while arr[left] < arr[pivot]:
            left += 1
        
        # find the first right element that's less than pivot
        while arr[right] < arr[pivot]:
            right += 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left] 
        else:
            break

    # swap left pointer and pivot
    arr[pivot], arr[left] = arr[left], arr[pivot]

    quick_sort(arr, 0, n/2)
    quick_sort(arr, n/2, n)


    return arr

if __name__ == "__main__":
    quick_sort()