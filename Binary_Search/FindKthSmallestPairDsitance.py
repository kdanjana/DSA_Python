""" 
The distance of a pair of integers a and b is defined as the absolute difference between a and b.
Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] 
and nums[j] where 0 <= i < j < nums.length.
Input: nums = [1,6,1], k = 3
Output: 5
Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
"""


def smallestDistancePair(nums, k):
    def numberPairs(absDiff):
        #returns number of pairs with absolute difference  <= absDiff 
        count = 0
        #using sliding window
        l = 0
        r = 1
        while l < len(nums) and r < len(nums):
            if abs(nums[r]-nums[l]) <= absDiff:
                count += (r-l)
                r += 1
            else:
                l += 1
        #    print("count is", count)
        return count
    
    #binary search 
    nums.sort()
    low = 0
    high = abs(nums[-1]-nums[0])
    res = 0
    # print(nums)
    #u do binary search on the range between min and max absolute difference b/n pairs
    while low <= high:
        mid = low + ((high-low)//2)
        # print(f"low is {low}, high is {high}, mid is {mid}")
        # print(f"number of pairs that have diff <= {mid} are {numberPairs(mid)} k is {k}")
        if numberPairs(mid) >= k:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res

print(smallestDistancePair([1,3,7,8,21],3)) # [1,2,4,5,6,7,13,14,18,20]
print(smallestDistancePair([1,3,1],1))      # [0,2,2]
print(smallestDistancePair([1,1,6], 3))     # [0,5,5]

