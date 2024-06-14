""" 
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
explanation: room1: [0,30] room2:[5,10], [15,20]
Input: [[7,10],[2,4]]
Output: 1
 The goal is to find the minimum number of conference rooms required to accommodate all these meetings
 without any overlap. In other words, we want to allocate space such that no two meetings occur in the 
 same room simultaneously.
"""

# approach 1
def solve(intervals):
    # sort based on  start and end times from intervals
    startTimes = sorted(interval[0] for interval in intervals)
    endTimes = sorted(interval[1] for interval in intervals)
    # i will keep track of start times
    # j will keep track of endtimes
    i, j = 0, 0
    # at any given time number of rooms used by meetings
    rooms = 0
    # minimum number of rooms required to accomidate all meetings without any overlap
    res = 0
    # Traverse startTimes and endTimes
    while i < len(startTimes):
        #if start time of one meeting is < end time another meeting then u need a new room
        if startTimes[i] < endTimes[j]:
            rooms += 1
            res = max(res, rooms)
            i += 1
        else:
            #if start time of one meeting is > end time another meeting then u dont need a new room, u use same room
            rooms -= 1
            j += 1
    return res


# solution: https://www.youtube.com/watch?v=s8oOsWGHIl4&t=1083s

#using heaps
import heapq 

def numberOfRooms(intervals):
    # sort based on  start times
    intervals.sort()
    #minheap store endtimes
    pq = []
    heapq.heappush(pq, intervals[0][1])
    # minimum number of rooms required to accomidate all meetings without any overlap
    res = len(pq)
    # Traverse startTimes and endTimes
    for i in range(1,len(intervals)):
        if intervals[i][0] < pq[0]:
            heapq.heappush(pq, intervals[i][1])
        else:
            #u can use same room, pop old meeting and push current meeting
            heapq.heappop(pq)
            heapq.heappush(pq, intervals[i][1])
        res = max(res, len(pq))
    return res

