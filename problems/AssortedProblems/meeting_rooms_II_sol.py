'''
sol:
- visual representation of the meeting times 
on a timeline
- traverse the timeline from start to end
- keep track of how many meetings are currently going on
    if we see a meeting start, 
        increment count
    if we see a meeting end, 
        decrement count

return the max value that count held during this traversal

------------------------------------

pseudocode:
- keep track of 2 arrays:
start: all starting times sorted
end: all ending times sorted

- have 2 pointers, one at the beginning of each
if start < end,
    => meeting has started
    increment count
    move start pointer
if start == end,
    edge case, where a meeting both starts and ends
    end takes priority,
    decrement count
    move end pointer
if end < start,
    => meeting has ended
    decrement count
    move end pointer
once we've traversed through start times,
    we know we'll just be decrementing count
    so we can end the algo.

------------------------------------
Input: intervals = [(0,40),(5,10),(15,20)]
    starts = [0, 5, 15]
    ends = [10, 20, 40]

Output: 2


'''

from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

def minMeetingRooms(self, intervals: List[Interval]) -> int:
    if len(intervals) == 0:
        return 0

    starts = []
    ends = []

    # put all start and end times in respective arrays
    for i in range(len(intervals)):
        starts.append(intervals[i].start)
        ends.append(intervals[i].end)

    starts.sort()
    ends.sort()

    start_pointer = 0
    end_pointer = 0
    room_count = 0
    max_rooms = float("-inf")

    while start_pointer < len(starts):
        if starts[start_pointer] < ends[end_pointer]:
            # ie. a meeting has started
            room_count += 1
            start_pointer += 1
            if room_count > max_rooms:
                max_rooms = room_count

        elif starts[start_pointer] >= ends[end_pointer]:
            # ie. a meeting has ended
            # or if equal, a meeting ends AND starts
            room_count -= 1
            end_pointer += 1

    return max_rooms


'''
time complexity:
- one iteration to create starts, ends arrays. O(N)
- sorting O(NlogN)
- best case, one iteration through starts. O(N)
- worst case, iterate fully through both starts and ends. O(2N)

total:
O(N + NlogN + 2N)
= O(NlogN + 3N)
=> O(NlogN)

space complexity:
starts, ends are arrays that contain N items each
O(N + N)
= O(2N)
=> O(N)
'''