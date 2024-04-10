""" Design a class to find the kth largest element in a stream. """
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.size_pq = k
        heapq.heapify(self.pq)
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq,val)
        if len(self.pq) > self.size_pq:
            heapq.heappop(self.pq)
        return self.pq[0]
        