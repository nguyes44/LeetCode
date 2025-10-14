'''
problem:
you are climbing a staircase 
with n steps to reach the top
each time you can climb either 1 or 2 steps
how many distinct ways can you climb to the top?

--------------------------------------------------
input/output:
n=2
output: 2
expl:
1. 1+1
2. 2

n=3
output: 3
1. 1+1+1
2. 1+2
3. 2+1

--------------------------------------------------
custom input/output:
n=1
output: 1

n=4
output:
1. 1+1+1+1
2. 1+1+2
3. 1+2+1
4. 2+1+1
5. 2+2

n=5
1. 1+1+1+1+1

2. 1+1+1+2
3. 1+1+2+1
4. 1+2+1+1
5. 2+1+1+1

6. 1+2+2
7. 2+1+2

8. 2+2+1


n=8
1. 1+1+1+1+1+1+1+1

2. 1+1+1+1+1+1+2
3. 1+1+1+1+1+2+1
4. 1+1+1+1+2+1+1
5. 1+1+1+2+1+1+1
6. 1+1+2+1+1+1+1
7. 1+2+1+1+1+1+1
8. 2+1+1+1+1+1+1

9. 1+1+1+1+2+2
10. 1+1+1+1+2+2

--------------------------------------------------
pseudocode:
- we can start with the obvious case:
    all 1 steps, 1s-count = 5
- compress the last 2 steps into one
    1s-count = 3
- how many unique spots can this compressed step go into?
    ex. first compression of n=5 => 4 sols, 1s-count+1?

- compress the last 2 steps again
    1s-count= 1
    second compression of n=5 => 2 sols, 

1s-count is not even, so that leaves us with how many sols?


'''