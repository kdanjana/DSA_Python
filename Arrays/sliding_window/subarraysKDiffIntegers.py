""" 
Given an integer array nums and an integer k, return the number of good subarrays of nums. A good array 
is an array where the number of different integers in that array is exactly k.
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: 
[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
The trick here is to call the helper function f(k) twice: once for k and once for k-1 to find the number of 
windows with exactly k distinct integers and subtract the number of windows with exactly k-1 distinct integers.
The reason behind this is that by finding the difference between these two counts, we effectively calculate 
the number of new subarrays that have exactly k distinct integers, as any window with k-1 distinct integers 
cannot contribute to the count of windows with exactly k
"""


def subarraysWithKDistinct(nums, k):
    def countSubarraysOfAtmostPdistinct(p):
        res = 0
        l = 0
        r = 0
        window = {}
        while r < len(nums):
            window[nums[r]] = window.get(nums[r],0) + 1
            while len(window) > p:
                window[nums[l]] -= 1
                if window[nums[l]] == 0:
                    del window[nums[l]]
                l += 1
            res += (r-l+1)
            r += 1
        return res
        
    return countSubarraysOfAtmostPdistinct(k) - countSubarraysOfAtmostPdistinct(k-1)

print(subarraysWithKDistinct([1,2,1,2,3], 2))