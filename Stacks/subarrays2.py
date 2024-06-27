"""  
Sum of Subarray Maximums
Given an array of integers arr, find the sum of max(b), where b ranges over every 
(contiguous) subarray of arr. Since the answer may be large, return the answer 
modulo 109 + 7.
"""


def sumSubarrayMaxs(arr):
    res = 0
    n = len(arr)
    mod = 10**9 + 7
    left = [-1] * n
    right = [n] * n
    stk = []
    for i in range(n):
        while stk and arr[stk[-1]] <= arr[i]:
            stk.pop()
        if stk:           
            left[i] = stk[-1]
        stk.append(i)
    stk = []
    for i in range(n-1,-1,-1):
        while stk and arr[stk[-1]] < arr[i]:
            stk.pop()
        if stk:
            right[i] = stk[-1]
        stk.append(i)
    for i in range(n):
        res += arr[i] * (i-left[i]) * (right[i]-i)
    return res % mod 



print(sumSubarrayMaxs([11,81,94,43,3]))



"""  Maximum Subarray Min-Product
The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.
For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.
Given an array of integers nums, return the maximum min-product of any non-empty subarray of nums.
Since the answer may be large, return it modulo 109 + 7.
Input: nums = [1,2,3,2]
Output: 14
Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.


"""
def maxSumMinProduct(nums):
        # array containing : min number * (sum of numbers) in subarray
        n = len(nums)
        productArr = [0] * n
        right = [n] * n
        left = [-1] * n
        stk = []
        prefixSum = [0] * n
        for i in range(n):
            while stk and nums[stk[-1]] >= nums[i]:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        stk = []
        for i in range(n-1,-1,-1):
            while stk and nums[stk[-1]] > nums[i]:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)
        prefixSum[0] = nums[0]
        for i in range(1,n):
            prefixSum[i] = prefixSum[i-1] + nums[i]
        # print(left)
        # print(right)
        # print(prefixSum)
        for i in range(n):
            left_index = left[i] + 1 if left[i] != -1 else 0
            right_index = right[i] - 1 if right[i] != n else n - 1
            productArr[i] = nums[i] * (prefixSum[right_index] - prefixSum[left_index] + nums[left_index])
        return max(productArr) % (10**9 + 7)

print(maxSumMinProduct([2,3,3,1,2]))