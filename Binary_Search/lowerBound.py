""" 
You are given an array 'arr' sorted in non-decreasing order and a number 'x'.
You must return the index of lower bound of 'x'.
For a sorted array 'arr', 'lower_bound' of a number 'x' is defined as the smallest index 'idx' such 
that the value 'arr[idx]' >='x'. If all numbers are smaller than 'x', then 'n' should be the 
'lower_bound' of 'x', where 'n' is the size of array.
another way of asking is ----->
Problem statement
You are given a sorted array 'arr' of distinct values and a target value 'm'. You need to search for 
the index of the target value in the array. If the value is present in the array, return its index.
If the value is absent, determine the index where it would be inserted in the array while maintaining 
the sorted order. 
"""



def lowerBound(arr, x) -> int:
    # Write your code here
    res = len(arr)
    mid = 0
    low = 0
    high = len(arr) -1
    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[mid] >= x:
            res = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            # look on the right
            low = mid + 1
    return res

print(lowerBound([1, 2, 2, 3, 3, 5], 7))   # len of arr = 6
print(lowerBound([1, 2, 2, 3, 3, 5], 4))   # 5
print(lowerBound([2462, 3941, 4337, 6505, 11444, 12819, 13811, 18], 10063))   # 4
print(lowerBound([1, 2, 3, 3, 5, 7, 8, 8, 10, 10, 11], 9))   # 8
print(lowerBound([3, 5, 8, 9, 15, 19], 9)) # 3