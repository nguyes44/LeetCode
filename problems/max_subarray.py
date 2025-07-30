# Max Sum Subarray of Size K (easy)

# Problem Statement
# Given an array of positive numbers and a positive number ‘k,’ 
# find the maximum sum of any contiguous subarray of size ‘k’.

# Example Output:
# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

# Input: [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

# Pseudocode
# we will use sliding window since we need to compute something all contiguous subarrays
# we have a sliding window of size K
#   
# we'll keep track of a local sum and max sum

# begin to iterate over the input array
#   add the first element to the local sum
#   check if we've summed all of the elements for the sliding window yet
#   via counter? ie. sliding_window_size increment
#   if not, continue
#       if so, compare the local sum to the max sum
#       ie. is local sum > max sum?
#       => max sum should be init to -inf
#       on first instance, the local sum should always be loaded to the max sum
#
#       in the same conditional, remove the item that exited the sliding window 
#       via subtraction from the local sum

# print max sum

def main():
    print(max_sum_func([2, 3, 4, 1, 5], 2))
    return

def max_sum_func(input_array: list[int], k: int):
    local_sum = 0
    max_sum = -1

    for i in range(0, len(input_array)):
        local_sum += input_array[i]

        # check if we've summed the sliding window yet
        if i >= k - 1:
            if local_sum > max_sum:
                max_sum = local_sum
            
            # move sliding window
            local_sum -= input_array[i-1]

    return max_sum

main()