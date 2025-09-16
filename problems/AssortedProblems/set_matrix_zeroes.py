'''
problem:
given an m*n int matrix, 
if an element is 0,
set its entire row and column to 0's

do it in-place
(ie. modify the input matrix, don't make a copy)

--------------------------------
input/output:
input:
[
[1,1,1]
[1,0,1]
[1,1,1]
]
output:
[
[1,0,1]
[0,0,0]
[1,0,1]
]
we saw 2,2 has a 0,
so we'll clear the 2nd column and 2nd row

input:
[
[0,1,2,0]
[3,4,5,2]
[1,3,1,5]
]
output:
[
[0,0,0,0]
[0,4,5,0]
[0,3,1,0]
]
we saw 1,1 has a 0,
so we'll clear out the 1st row and column
then, 1,4 has a 0,
so we'll clear out the 1st row and 4th column

--------------------------------
custom input/output:
m := # rows
n := # columns
can assume they're valid matricies

input:
[
[1]
]
output:
[
[1]
]

--------------------------------
brute force pseudocode:
- iterate through each element, i,j
- when we run into a 0, 
    start clearing out the ith row
    clear out the jth column
- repeat until iterated over all elements

- this doesn't work out of the box

concerns:
- right after we set the 2nd row to 0, 
we'll check element 2,3, which we see is a 0
however, we do NOT want to clear rows and columns
based on this finding.
Because this 0 was not from the input,
rather from clearing

- need a way to know not to perform 
clearing based on this 0

- maybe we can store rows and columns to pass?
    i think this raises a problem of 
    ignoring an input 0 in the 2nd sample input

- we'd clear the 1st row, 1st column, then ignore
however, we see that we have an input 0 at 1,4.
we'd completely miss this clearing.

--------------------------------

new brute force pseudocode:
- iterate through each element to find the input 0s
when an input 0 is found, 
    record its row and column for future ref
- for each number, i, in rows,
    clear the ith row
- same for column


'''

from typing import List

def setZeroes(self, matrix: List[List[int]]) -> None:
    clear_rows = set()
    clear_columns = set()

    # iterate over each element
    # initially to find the input 0s
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                clear_rows.add(i)
                clear_columns.add(j)

    # now, iterate over clear_rows
    # begin clearing rows
    for k in clear_rows: # ie. for each row,
        # say, we have k=2 from first input
        for l in range(len(matrix[k])): # ie. for each element in row
            matrix[k][l] = 0
    
    for o in clear_columns: # ie. for each column
        # say, we have o=2 from first input
        for p in range(len(matrix)):
            matrix[p][o] = 0

    return # nothing, modify in-place


'''
time complexity:
- iterate over each element once initially
m*n elements

- iterate over a row for each input 0
    w/ unique row number
n elements * unique row numbers

- iterate over a column for each input 0 
    w/ unique column number
m elements * unique column numbers

=> O(m*n + n*unique row no. + m*unique column no.)
=> O(m*n)

space complexity:
- rows = unique row numbers
    worst case, O(m)
- columns = unique column numbers
    worst case, O(n)
=> worst case: O(m+n)
typically less

--------------------------------
optimal sol w/ O(1) space:
- we want to store the info of the arrays "rows" and "columns"
    inside the actual input array
- we use the top and left most values of the matrix to store
    this info.
- however, there will be an overlapping value at 1,1.
    we use a single variable to denote the columns value

- iterate through each element
- once we run into a 0, we'll write 0 onto the respective top and left values
    ex. get a 0 at 2,2
    set matrix[0][1] = 0
    matrix[1][1] = 0

- we are safe to do this and not create non-input 0s that affect the result
this is because when we iterate, we have already seen the top and left most values.
therefore they can't trigger a clearing effect.
we only trigger a clearing effect when we SEE a 0
we will never see a non-input 0

'''

def setZeroes(matrix: List[List[int]]) -> None:
    row_cell = False
    m = len(matrix) # no. rows
    n = len(matrix[0]) # no. columns

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                # if we have to clear the 1st row,
                # ie. i == 0
                # then we'll set row_cell = True
                if i == 0:
                    row_cell = True
                else:
                    matrix[i][0] = 0

                matrix[0][j] = 0
    
    # start clearing rows
    # traverse the first column
    for l in range(1, m):
        if matrix[l][0] == 0:
            for o in range(n):
                matrix[l][o] = 0

    # start clearing columns
    for p in range(1, n):
        # go through the top most row
        if matrix[0][p] == 0:
            for q in range(m):
                matrix[q][p] = 0

    # clear first column if necessary
    if matrix[0][0] == 0:
        for z in range(m):
            matrix[z][0] = 0

    # clear first row if necessary
    if row_cell:
        for k in range(n):
            matrix[0][k] = 0

    return

'''
time complexity:
- m*n for initial iteration over all elements

'''

