""" 
You are given an array 'arr' sorted in non-decreasing order and a number 'x'.
You must return the index of lower bound of 'x'.
For a sorted array 'arr', 'lower_bound' of a number 'x' is defined as the smallest index 'idx' such 
that the value 'arr[idx]' is not less than 'x'. If all numbers are smaller than 'x', then 'n' should be the 
'lower_bound' of 'x', where 'n' is the size of array.

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
            high = mid - 1
        else:
            low = mid + 1
    return res

print(lowerBound([1, 2, 2, 3, 3, 5], 7))   # len of arr = 6
print(lowerBound([1, 2, 2, 3, 3, 5], 4))   # 5
print(lowerBound([2462, 3941, 4337, 6505, 11444, 12819, 13811, 18], 10063))   # 4
print(lowerBound([1, 2, 3, 3, 5, 8, 8, 10, 10, 11], 9))   # 7