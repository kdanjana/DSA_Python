""" 
You are given a sorted array ‘arr’ containing ‘n’ integers and an integer ‘x’. Implement the ‘upperBound’ 
function to find the index of the upper bound of 'x' in the array.
Note:
The upper bound in a sorted array is the index of the first value that is greater than a given value. 
If the greater value does not exist then the answer is 'n', Where 'n' is the size of the array.
We are using 0-based indexing.
Try to write a solution that runs in log(n) time complexity.
"""


def upperBound(arr, x):
    # Write your code here.
    res = len(arr)
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = low + ((high-low) // 2)
        if arr[mid] > x:
            res = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            # look on the right
            low = mid + 1 
                  
    return res


print(upperBound([3, 5, 8, 9, 15, 19], 9))   # 4