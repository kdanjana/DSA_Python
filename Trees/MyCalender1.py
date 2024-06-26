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


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MyCalendar:
    def __init__(self):
        self.calender = Node()

    def book(self, start: int, end: int) -> bool:
        pointer = self.calender
        while True:
            if pointer.left is None and pointer.right is None:
                pointer.left = Node(start)
                pointer.right = Node(end)
                return True
            if start >= pointer.right.val:
                pointer = pointer.right
            elif end <= pointer.left.val:
                pointer = pointer.left
            else:
                return False