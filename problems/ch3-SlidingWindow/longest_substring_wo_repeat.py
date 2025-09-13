'''
problem:
Given string s,
find the length of the longest substring
without duplicate characters

-------------------------------------
input/output:
s = "abcabcbb"
output: 3
expl:
- "abc" is the longest substring without dupes

s = "bbbb"
output: 1
expl. "b" is the longest substring without dupes

s = "pwwkew"
output: 3
expl. "wke" is the longest substring without dupes

-------------------------------------
custom input/output:
s = ""
output: 0

s = "aaaaaab"
output: 2

-------------------------------------
pseudocode:
- keep a set "substring" initially empty
- keep a "max_length" count, initially 0 
- iterate through the string s
- attempt to add the character to the set
- we expect the set's length to change.
    - keep track via "current_length"
- if it hasn't changed, then reset the count to 1
- if it has changed, do nothing

'''

# def lengthOfLongestSubstring(s: str) -> int:
#     substring = set([])
#     max_length = 0
#     current_length = 0

#     for i in range(len(s)):

#         current_length += 1
#         substring.add(s[i])        

#         if len(substring) != current_length:
#             # ie. we tried to add a redundant character

#             # update our max_length so far if we can
#             if current_length - 1 > max_length:
#                 max_length = current_length - 1

#             # reset our streak
#             current_length = 1
#             substring = {s[i]}

#             # begin iterating backwards
#             j = i - 1 # j is c
#             while j >= 0:
#                 # try to add previous char
#                 current_length += 1
#                 substring.add(s[j])
#                 j -= 1


#                 if len(substring) != current_length:
#                     # update our max_length so far if we can
#                     if current_length - 1 > max_length:
#                         max_length = current_length - 1

#                     break
#                 else:
#                     # our character was added successfully
#                     if current_length > max_length:
#                         max_length = current_length

#         else:
#             # our character was added successfully
#             if current_length > max_length:
#                 max_length = current_length

#     return max_length


'''
failed test case:
s= " "
why is this different from "a"?

- need to run through locally and print it out

----------------------

s="dvdf"
- when we're at s[2]=d
substring = {d, v}
we see that we have a redundant character
we reset the substring to be = {d}
however, this is incorrect, as then we'll have the substring 
{d, f} as longest.

although in reality, {v, d, f} was longest

- at s[2]=d, we need to know to go back somehow
    can we keep going back until we run into another redundant char?
    increment current_length, add to substring


----------------------
s="abcabcbb"
output: 4
exp: 3


    

----------------------
completely alternate brute force approach:
- for each character,
iterate and increment until reached a redundant character.
=> essentially N^2 sol.



'''

# brute force approach
def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0

    current_substring = set()
    max_length = 1

    for i in range(len(s)):
        current_length = 1
        current_substring = {s[i]}

        j = i + 1
        while j < len(s):

            if s[j] not in current_substring:
                current_length += 1
                current_substring.add(s[j])
            else:
                if current_length > max_length:
                    max_length = current_length
                break

            j += 1
            if current_length > max_length:
                max_length = current_length

    return max_length

def main():
    print(lengthOfLongestSubstring("au"))

    return

main()

'''
time complexity:
- iterate through each character, i
    - iterate through each next character, j, until streak ends
=> O(N * avg substring length)
almost O(N^2) ?

space complexity:
- storing the substring in a set
=> O(max substring length)
worst case O(N)
when the whole string is the longest substring

----------------------
IMPROVING BRUTE FORCE:
in s='abcabcbb'
- let's say we're at 'abca'
- we end the check
- reset to b
- iterate until we get 'bcab'

- instead of resetting to b, 
we already know that 'bca' is a non-repeating substring

- we'll reset i to bca,
    but j will be at bcaB instead

- when we're at abc and get b, we'll reset to cb
    we need to cut out the left end of the string 
    that contains the colliding char, inclusive

- this is literally sliding window
'''


def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0
    
    max_length = 1
    current_char_set = {s[0]}
    current_substring = s[0]

    for i in range(1, len(s)):

        if s[i] not in current_char_set:
            current_char_set.add(s[i])
            current_substring += s[i]
        else:
            if len(current_substring) > max_length:
                max_length = len(current_substring)

            while s[i] in current_char_set:
                # pop it from the back
                popped_char = current_substring[0]
                current_char_set.remove(popped_char)
                current_substring = current_substring[1:]

            # add collision char to the end
            current_char_set.add(s[i])
            current_substring += s[i]


    if len(current_substring) > max_length:
        max_length = len(current_substring)

    return max_length


'''
time complexity:
- iterate once across the string
    - on each iteration, we'll eventually have to remove characters
    - removing characters will go on until the colliding char is removed

almost O(N)?

space complexity:
- store the substring
- store the char set
worst case; O(2N)
=> O(N)

- we observe that this problem is sliding window, 
    because it deals with contiguous "subarrays" ie. substrings


'''
