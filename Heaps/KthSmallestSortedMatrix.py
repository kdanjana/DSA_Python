""" 
Given an n x n matrix where each of the rows and columns is sorted in ascending order,
return the kth smallest element in the matrix. Note that it is the kth smallest element in the sorted order,
not the kth distinct element.
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
"""


import heapq

def kthSmallest(matrix, k):
    #using max heap, TC=O(nlogk), sc=o(k)
    heap = []
    for row in matrix:
        for num in row:
            heapq.heappush(heap, -num)
            if len(heap) > k:
                heapq.heappop(heap)
    return -heapq.heappop(heap)
    #my approach using minheap
    # pq = []
    # rows = len(matrix)
    # cols = len(matrix[0])
    # for r in range(rows):
    #     for c in range(cols):
    #         heapq.heappush(pq,matrix[r][c])
    # res = 0
    # while k > 0:
    #     res = heapq.heappop(pq)
    #     k -= 1
    # return res
        
print(kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))