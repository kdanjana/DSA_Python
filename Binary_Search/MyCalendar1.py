""" 
You are implementing a program to use as your calendar. We can add a new event if adding the event will not
cause a double booking. A double booking happens when two events have some non-empty intersection 
(i.e., some moment is common to both events.). The event can be represented as a pair of integers start and 
end that represents a booking on the half-open interval [start, end), the range of real numbers x such that 
start <= x < end.
Implement the MyCalendar class:
MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully
without causing a double booking. Otherwise, return false and do not add the event to the calendar.
"""

#using Binary Search
class MyCalendar:

    def __init__(self):
        self.calender = []
        

    def book(self, start: int, end: int) -> bool:
        l = 0
        r = len(self.calender)
        #using BS we are trying to find the index(l) at which we can insert the
        #(start,end) in the self.calender
        while l < r:
            mid = l + ((r-l)//2)
            if self.calender[mid][0] <= start:
                l = mid + 1
            else:
                r = mid 
        #once we find the index(l) at which we can insert new event, we check if events
        # intersect if we insert the event at that index(l)
        if self.intersects(l,start,end):
            return False
        else:
            self.calender.insert(l, (start,end))
        return True

    def intersects(self,index,start,end):
        #  Collision with previous interval or Collision with next interval
        return ((self.calender[index-1][1] > start if index > 0 else False) or 
            (self.calender[index][0] < end if index <len(self.calender) else False))
        


# my approach
# class MyCalendar:

#     def __init__(self):
#         self.events = []
        

#     def book(self, start: int, end: int) -> bool:
#         if len(self.events) > 0:
#             for i in range(len(self.events)):
#                 if self.events[i][1] > start and self.events[i][0] < end:
#                     return False
#         self.events.append((start,end))
#         return True
    
    
    