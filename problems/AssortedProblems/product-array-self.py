'''
problem:
given an integer array "nums"
return an array "answer" such that 
    answer[i] is equal to the product of all elements of nums
    except nums[i]

the product is guaranteed to fit in a 32-bit integer.

Run in O(n) time.
Do not use the division operation.

--------------------------------------------
input/output:
nums=[1,2,3,4]
answer=[24,12,8,6]

nums=[-1,1,0,-3,3]
answer=[0,0,9,0,0]

custom input/output:
nums=[5,3]
answer=[3,5]

nums=[0,1,2,3,4,0]
answer=[0,0,0,0,0,0]

observation:
- if there is a 0 in the array,
    all products will be 0 except for i where 0 is excluded
- if there are 2+ 0s in the array,
    all products will be 0

--------------------------------------------

brute force pseudocode:
answer=[]

for each i=0,
    if i=0
        product = nums[1]
    else
        product = nums[0]

    for each j != i
        product = product * nums[j]

    answer.append(product)

- this approach is O(N^2) since for each i, 
    we iterate essentially over the whole array

--------------------------------------------    
suggestion:
- why don't we somehow reuse the product that we previously 
    computed? similar to sliding window's approach

for each i=0
    if i=0
        compute the initial product
    else
        remove the previous product
        (ie. do the opposite operation, division)
        can't divide, so can we do repeated subtraction?
        i don't think so, that would be long runtime.
        ex. removing 10 from 10 * 100 = 1000 would initially mean
        1000/10 = 100
        but repeated subtraction would be 1000 - 10 90 times, infeasible
        can we still replicate division somehow?

    
let's say we have 
nums=[1,2,3,4]
    i=0,
    product = 2*3*4
            = 24
    i=1,
    need to remove 2 from 2*3*4
    and add in 1 to the product.

    
for i=0, why don't we keep 3*4 for the next iteration?
    we know we'll have to compute that next time.
    keep the 'sub_product' so we avoid iterating again

nums=[1,2,3,4]
    i=0
    add 3 to the sub_product
    add 4 to the sub_product
    product = 2*sub_product

    i=1
    product = 1*3*4
            = 1*sub_product
    i=2
    product = 1*2*4
    had to remove 3 from sub_product (how?)

--------------------------------------------
there is the concept of 'prefix' and 'suffix' products


the problem is that let's say i have the product 3*4*5
i need to be able to remove 3 and get the result 4*5 instead
WITHOUT division.
    



'''