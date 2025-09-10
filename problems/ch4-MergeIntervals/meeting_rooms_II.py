'''
problem:
Given an array of meeting time interval objects w/ 
start and end times [[start_1,end_1], [start_2,end_2], ...]
where (start_i < end_i)

find the minimum number of days required to 
schedule all meetings without any conflicts

Note:
(0,8) and (8,10) is NOT a conflict at 8

---------------------------
input/output:
intervals = [(0,40), (5,10), (15,20)]
output: 2
expl:
- if we look at (0,40), 
we notice that we can't fit any of (5,10) or (15,20) in, 
as (0,40) takes the whole day
=> we can have on day 1: (0,40)

- looking at (5,10), 
we see that we can fit in another meeting, (15,20)
as there are no conflicts

=> day 2: (5,10), (15,20)

----
intervals = [(4,9)]
output: 1
expl: there is only 1 meeting, so only 1 day is required.

---------------------------
custom input/output:
intervals = []
output: 0

intervals = [(0,40), (0,40)]
output: 2

intervals = [(0,40), (0,40), (0,40)]
output: 3



---------------------------
basic merge interval algorithm:
1. sort the intervals based on start times
2. begin with the first interval, A
3. compare the end time of interval A with 
    start time of interval B
    determine if there is a "conflict"
    if conflict AND end time of B > end time of A, 
        then 'merge' intervals
    ex. (0,5), (2,3) conflict
    => (0,5), merged without taking end time
    ex. (0,5), (2,6) conflict
    => (0,6), merged by taking end time.

4. continue for each interval

---------------------------
pseudocode:
- i believe we'd work with the merge intervals algo.

1. sort the intervals based on start times
2. begin with the first interval, A
3. compare the end time of A w/
    start time of B
    determine if there is a conflict
    if so, then we'd increment a "days_required" counter
    if not, do nothing
4. move onto the next interval and repeat until done

'''





from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

def minMeetingRooms(self, intervals: List[Interval]) -> int:
    if len(intervals) == 0:
        return 0
    days_required = 1
    days = []

    # sort the intervals based on start times
    intervals.sort(key=lambda x: x.start)

    # iterate over intervals,
    # checking for conflicts
    # incrementing days_required as conflicts arise
    current_day = []
    for i in range(len(intervals)):
        # first, check if the next interval is a valid access
        # then, compare the end of first interval w/
        # start of second interval to check conflict
        if i+1 < len(intervals)-1 and intervals[i].end > intervals[i+1].start:
            days_required+=1
            current_day.append(intervals[i])
            days.append(current_day)
            current_day = []

        # add to current day if no conflict
        elif i+1 < len(intervals)-1 and intervals[i].end <= intervals[i+1].start:
            current_day.append[intervals[i]]

        # on last interval,
        # we've processed all meetings prior incl. this one for conflicts
        # add to current day and finalize the schedule
        elif i == len(intervals)-1:
            current_day.append(intervals[i])
            days.append(current_day)

    # iterate over all days
    # compare the end of jth day to start of all days
    for j in range(len(days)):
        for k in range(len(days)):
            if j != k and days[j][-1].end <= days[k][0].start:
                days_required-=1
                # combine the days
                # how do i combine the days?
                # if i append day4 onto day1, i should wipe day4.
                # but if i wipe day4, then this messes up the iteration
                
                # a solution could be to create a copy.
                # this DOESNT violate the O(N) memory requirement, 
                # as we'll be O(2N)

            # but now, there's the problem of combining A, B, 
            # then C combines with B
            # but B is not encapsulated into A

    return days_required

'''
failed test case:
intervals=[(1,5),(5,10),(10,15),(15,20),(1,20),(2,6)]
my output: 4
expected: 3

intervals.sort = [(1,5),(1,20),(2,6),(5,10),(10,15),(15,20)]

day1: [(1,5)]
day2: (1,20)
day3: (2,6)
day4: [(5,10), (10,15), (15,20)]

apparently, there is a way to fit this in 3 days. i'm clearly missing something, so how?
oh shit. I can put (1,5) into (5,10)

when i'm at i=0, (1,5)
i'm comparing end time of A to start of B
how can i know to combine (1,5) and (5,10)?

maybe another iteration over the days
for each day, 
compare the end of the WHOLE day to the start of each other day.

'''