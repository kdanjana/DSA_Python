""" 
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

def search(nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + ((high - low) // 2)
            if nums[mid] == target:
                return mid
            #identify which half is sorted
            if nums[low] <= nums[mid]:# left side is sorted
                # check if target lies on the left side
                if nums[low] <= target <= nums[mid]:
                    # if target lies on left side move to left side
                    high = mid - 1
                else:
                    # else move to right half
                    low = mid + 1
            else:# right side is sorted
                if nums[mid] <= target <= nums[high]: # check if target lies on right side
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
    
print(search([4,5,6,7,0,1,2], 0))  # 4