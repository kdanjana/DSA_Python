"""Find median of data stream at any given time.
intution:
we need a data structure that allows quick access to the middle elements. 
We use two heaps: a max heap to store the smaller half of the numbers and a min heap to store the larger half.
This way, the largest number in the smaller half or the smallest number in the larger half can easily give us the median.
In Python, the default heapq module provides a min heap implementation. To get a max heap , we insert negatives of the numbers into a heap.
"""

from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        # max heap that stores smaller elements(simulated with negative values)
        self.small = []  
        # min heap that stores larger elements
        self.large = []  

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)  
        # Move the largest element of small (max heap) to large (min heap)
        heappush(self.large, -heappop(self.small))
        # If large heap has more elements, move the smallest element of large to small
        if len(self.large) > len(self.small):
            heappush(self.small, -heappop(self.large))

    def findMedian(self) -> float:
        # If the heaps have equal size, the median is the average of the two heap's top elements
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]
