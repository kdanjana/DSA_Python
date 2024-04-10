""" You are given an integer array heights representing the heights of buildings, some bricks, 
and some ladders. You start your journey from building 0 and move to the next building by possibly using 
bricks or ladders.Return the furthest building index (0-indexed) you can reach if you use the given ladders and 
bricks optimally
"""
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # use ladder for higher height differences
        # use bricks only after ladders are exhausted
        minHeap = []
        heapq.heapify(minHeap)
        heightDiff = 0
        for i in range(len(heights)-1):
            heightDiff = heights[i+1] - heights[i]
            if heightDiff > 0:
                heapq.heappush(minHeap,heightDiff)
                if len(minHeap) > ladders:  # means we have used all our ladders
                    lowestHeightDiff = heapq.heappop(minHeap)
                    bricks -= lowestHeightDiff #after ladders are used now u count number of  bricks to jump
                    if bricks < 0:  # means u used all bricks also
                        return i
        return len(heights)-1