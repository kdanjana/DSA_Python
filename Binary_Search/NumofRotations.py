""" 
You are given an array 'arr' having 'n' distinct integers sorted in ascending order. The array is right 
rotated 'r' times. Find the minimum value of 'r'. Right rotating an array means shifting the element at 
'ith' index to (‘i+1') mod 'n' index, for all 'i' from 0 to ‘n-1'.
Example:
Input: 'n' = 5 , ‘arr’ = [3, 4, 5, 1, 2]
Output: 3 
Explanation:
If we rotate the array [1 ,2, 3, 4, 5] right '3' times then we will get the 'arr'. Thus 'r' = 3.
"""

def findKRotation(arr : [int]) -> int:
    # Write your code here.
    low, high = 0, len(arr) - 1
    res = len(arr)
    minVal = arr[0]
    while low <= high:
        mid = low + ((high-low)//2)
        if arr[low] <= arr[mid]:
            if arr[low] <minVal:
                minVal = arr[low]
                res = low
            low = mid + 1
        else:
            if arr[mid] < minVal:
                minVal = arr[mid]
                res = mid
            high = mid - 1
    if res == len(arr): # means rotated len(arr) times
        return 0 
    else:
        return res
