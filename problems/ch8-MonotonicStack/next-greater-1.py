'''
problem:
Next greater element of X: 
    first greater element that is to the right of X in the same array.

Given:
Two distinct arrays; nums1, nums2.
nums1 is a subset of nums2

For each item in nums1, 
    find the index j such that nums1[i] == nums2[j]
    determine the next greater element of nums2[j]
    if none, then answer is -1

return an array "ans" of length nums1.length
    ans[i] is the next greater element

------------------------------------------
input:
nums1 = [4,1,2]
nums2 = [1,3,4,2]

output:
[-1, 3, -1]
explanation:
- first, we start with nums1[0]=4
    we see that nums2[2]=4
    there is no next greater element of 4, so -1
- nums1[1]=1
    we see nums2[0]=1
    the next greater element is 3
- nums1[2]=2
    nums[3]=2
    no next greater element, -1

input:
nums1 = [2,4]
nums2 = [1,2,3,4]

output:
[3,-1]
explanation:
- nums1[0]=2
    nums2[1]=2
    next greatest element is 3
- nums2[1]=4
    nums2[3]=4
    no next greatest element, -1

custom input/output:
input:
nums1=[]
nums2=[1,2,3,4]
output:
[]

input:
nums1=[1,2,3,4]
nums2=[1,2,3,4]
output:
[2,3,4,-1]


------------------------------------------
DSA:
We know its a stack, but how do we utilize it?

------------------------------------------
pseudocode:
- we definitely have to iterate over nums1 to process all of the output
    => O(nums1.length)

- the brute force approach to finding the next greater element is to:
    -iterate over nums2 to find the matching element
    -iterate over that element's neighbours to find the next greater element
    =>O(nums2.length * nums1.length) total







'''