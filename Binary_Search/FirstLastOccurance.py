"""" 
Given an array of integers nums sorted in non-decreasing order, find the starting 
and ending position of a given target value. If target is not found in the array,
return [-1, -1]. You must write an algorithm with O(log n) runtime complexity.
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

def searchRange( nums, target):
    def lastOccurance(nums,target):
        # upperbound
        low = 0
        high = len(nums) - 1
        res = len(nums)
        while low <= high:
            mid = low + ((high - low) // 2)
            if nums[mid] > target:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
        
    def firstOccurance(nums,target):
        # lower bound of target
        low = 0
        high = len(nums) - 1
        res = len(nums)
        while low <= high:
            mid = low + ((high - low) // 2)
            if nums[mid] >= target:
                res = mid
                high = mid -1 
            else:
                low = mid + 1
        return res
        
        
    lowerBound = firstOccurance(nums,target)
    upperBound =  lastOccurance(nums,target)
    if lowerBound == len(nums) or  nums[lowerBound] != target:
        return [-1,-1]
    else:
        return [lowerBound, upperBound-1]
        
print(searchRange([5,7,7,8,8,10], 8))
print(searchRange([5,7,7,8,8,10], 9))
print(searchRange([5,7,7,8,8,10], 10))