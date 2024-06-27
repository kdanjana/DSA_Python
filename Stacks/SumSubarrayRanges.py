"""  
Sum of Subarray Ranges
You are given an integer array nums. The range of a subarray of nums is the difference 
between the largest and smallest element in the subarray.
Return the sum of all subarray ranges of nums.
A subarray is a contiguous non-empty sequence of elements within an array
Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
intution:
(sum of all subarray maxs -  sum of all subarrays mins )
"""


from subarrays1 import sumSubarrayMins
from subarrays2 import sumSubarrayMaxs


def subArrayRanges(arr):
    maxSum = sumSubarrayMaxs(arr)
    minSum = sumSubarrayMins(arr)
    return maxSum - minSum

print(subArrayRanges([1,2,3]))