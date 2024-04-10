""" Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0)."""
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        res = []
        heapq.heapify(min_heap)
        for i in range(len(points)):
            x,y = points[i]
            dist = (x ** 2) + (y ** 2)
            heapq.heappush(min_heap,(dist, x, y))
        while k > 0:
            dist, x, y = heapq.heappop(min_heap)
            res.append([x,y])
            k -= 1
        return res