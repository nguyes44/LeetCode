'''
problem:
given an m*n 2d binary grid 
representing a map of 1s (land) and 0s (water)
return the number of islands

An island a connected set of 1s (lands), 
either vertically or horizontally.

-------------------------------------
pseudocode:
- we'll have to iterate over the matrix
- use DFS when we detect an island (ie. find a 1)

when we run into a 1:
    - increment the island counter
    - turn it into a 0 to mark as visited
    - use DFS to find all other connected 1s of that island
    - mark them to 0

do nothing when we run into a 0

DFS Pseudocode:
- mark node as visited
- for each neighbour of node: 
    if neighbour is not visited (ie. if it's 1)
        DFS(neighbour)

Q's
- how do we access the neighbours of a matrix entry?
    a matrix entry (i,j) has neighbours 
    above & below (ie. i-1, i+1), 
    then left & right (ie. j-1, j+1)
when we search for neighbours, 
    we need to be sure that the index accesses are valid.
'''

from typing import List

def numIslands(grid: List[List[str]]) -> int:
    island_count = 0
    m = len(grid) # num of rows
    n = len(grid[0]) # num of columns
    # ex. [
    # [1,1,1], 
    # [1,1,1], 
    # [1,1,1], 
    # [1,1,1]
    # ]
    # m=4, n=3

    def DFS(i: int, j: int) -> None:
        grid[i][j] = "0" # mark current node as visited

        # define all neighbours for this node
        neighbour_list = [
            (i-1, j), # above 
            (i+1, j), # below
            (i, j-1), # left
            (i, j+1)  # right
            ]
        for neighbour in neighbour_list:
            if (0 <= neighbour[0] < m) and (0 <= neighbour[1] < n): # ie. if our accesses are valid
                if grid[neighbour[0]][neighbour[1]] == "1": # ie. the land is also not visited
                    DFS(neighbour[0], neighbour[1])

        return


    # traverse the matrix
    for row_no in range(0, m):
        for col_no in range(0, n):

            if grid[row_no][col_no] == "1":
            # ie. we run into an island
                island_count += 1

                DFS(row_no, col_no) # run DFS to find all connected land and mark 0

    return island_count


'''
failed test case:
[
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]
]
expected: 1
actual: 0

walkthrough
- begin matrix traversal

grid[row_no][col_no] should = 1
grid[0][0]

-------------------------------------
failed test case:
[
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]
]
expected: 1
actual: 6

- immediately run into an island, increment.
- run DFS on grid[0][0] to mark connected land
    - marks grid[0][0] to 0
    - defines neighbours 
    [
        (-1, 0) # above
        (1, 0)  # below
        (0, -1) # left
        (0, 1)  # right
    ]
    check validity:
        no, neighbour[0] not in range
        neighbour[0] in range, neighbour[1] in 
        oh im dumb, my valid range definition was 1 off.
'''

if __name__ == "__main__":
    grid =  [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ]
    
    print(numIslands(grid))


'''
time complexity:
- we have to iterate the matrix regardless, so m*n
- worst case: when we run into an island and have to mark all to 0
    imagine the whole grid was an island
    so m*n markings

O(2m*n) => O(m*n)

space complexity:
- almost constant, as we have constant num of variables.
- however, we use DFS, which has a worst-case recursive depth of m*n
=> O(m*n)

'''
