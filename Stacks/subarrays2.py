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