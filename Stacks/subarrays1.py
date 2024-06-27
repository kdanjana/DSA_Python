"""   
Sum of Subarray Minimums
Given an array of integers arr, find the sum of min(b), where b ranges over every 
(contiguous) subarray of arr. Since the answer may be large, return the answer 
modulo 109 + 7.
Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17
intution:
Solving this problem efficiently requires an understanding that each element of the array will be the minimum in some number of subarrays. So, rather than considering every subarray explicitly, we conceptualize the problem around each element of the array and determine how many subarrays it is the minimum element of.

To arrive at the solution, we must track two things for each element arr[i]:

left[i]: the index of the first smaller element to the left of arr[i]
right[i]: the index of the first element that is less than or equal to arr[i] to the right
With left[i] and right[i] determined, the number of subarrays in which arr[i] is the minimum can be 
calculated by (i - left[i]) * (right[i] - i).
"""


def sumSubarrayMins(arr):
    n = len(arr)
    # stack that stores index of prev smaller ele
    left = [-1] * n
    # stack that stores index of next smaller ele
    right = [n] * n
    stk = []
    for i in range(n):
        while stk and arr[stk[-1]] >= arr[i]:
            stk.pop()
        if stk:
            left[i] = stk[-1]
        stk.append(i)

    stk = []
    for i in range(n - 1, -1, -1):
        while stk and arr[stk[-1]] > arr[i]:
            stk.pop()
        if stk:
            right[i] = stk[-1]
        stk.append(i)
    print(left, right)
    mod = 10**9 + 7
    res = 0
    for i,val in enumerate(arr):
        res += val * (i - left[i]) * (right[i]- i)
    return res % mod 
            
        
   


print(sumSubarrayMins([11,81,94,43,3]))



