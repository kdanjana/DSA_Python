""" 
Given an n x n matrix where each of the rows and columns is sorted in ascending order,
return the kth smallest element in the matrix. Note that it is the kth smallest element in the sorted order,
not the kth distinct element.
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
intution:
Binary search comes to the rescue here, but instead of the regular binary search on a list, we apply it to a 
value range from the smallest element in the matrix (the top-left corner) to the largest element 
(the bottom-right corner). The crucial observation is that every element less than or equal to a value mid 
within this range qualifies as a candidate for being one of the k smallest elements. The helper function 
essentially counts how many elements in the matrix are less than or equal to mid. This count is compared 
with k to decide if we need to search higher or lower. Each time, we adjust the value of mid and repeat 
the process, converging on the value of the kth smallest element. The logic being, if there are at least 
k numbers less than or equal to mid, then the kth smallest number is at most mid.
"""


def kthSmallest(matrix, k) -> int:
         # Helper function to count the number of elements smaller or equal to mid
        def count_less_equal(mid, k, size):
            count = 0
            row, col = size - 1, 0  # Start with the bottom-left corner of the matrix
          
            while row >= 0 and col < size:
                if matrix[row][col] <= mid:
                    count += row + 1  # Add all the elements of the current column
                    col += 1  # Move to the next column
                else:
                    row -= 1  # Move to the previous row
          
            return count >= k  # Check if the count is greater than or equal to k

        size = len(matrix)
        # Set initial binary search bounds
        low, high = matrix[0][0], matrix[size - 1][size - 1]
        res = 0
        # Perform binary search
        while low <= high:
            mid = (low + high) // 2  # Choose the middle value
            # If the count of numbers less than or equal to mid is k or more
            if count_less_equal(mid, k, size):
                res = mid
                high = mid - 1  # Narrow down the search space to the lower half
            else:
                low = mid + 1  # Narrow down the search space to the upper half
      
        return res  # The kth smallest number
    
    
print(kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))