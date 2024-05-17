""" 
You are given a sorted array consisting of only integers where every element appears exactly twice, 
except for one element which appears exactly once. Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
INtution:
The pairs which are on the left of the single element, will have the first element in an even position and the
second element at an odd position. All the pairs which are on the right side of the single element will have 
the first position at an odd position and the second element at an even position. Use this fact to decide 
whether to go to the left side of the array or the right side.
The key insight here is to understand how pairs of the same numbers are arranged 
in the array. Since the array is sorted, identical numbers are adjacent. If we take the first 
occurrence of a pair, it should be at an even index, and its pair should be immediately next, 
at an odd index, and this pattern continues until we hit the single element. After the single 
element, this pattern will flip because of the missing pair
"""


def singleNonDuplicate(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[-1] != arr[-2]:
        return arr[-1]
    left = 1
    right = n - 2
    while left <= right:
        mid = left + ((right-left)//2)
        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]
        if mid % 2 == 0:
            if arr[mid] != arr[mid+1]:
                right = mid - 1
            elif arr[mid] == arr[mid+1]:
                left = mid + 1
        else:
            if arr[mid] != arr[mid-1]:
                right = mid - 1
            elif arr[mid] == arr[mid-1]:
                left = mid + 1
        
    return -1


print(singleNonDuplicate([3,3,7,7,10,11,11]))