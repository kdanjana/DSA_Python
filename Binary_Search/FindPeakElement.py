def findPeakElement(nums):
        low = 0
        high = len(nums) - 1
        if len(nums) == 1:
            return 0
        
        while low <= high:
            mid = (low + ((high - low) // 2))
            #if first ele is peak
            if mid == 0:
                if nums[mid] >  nums[mid+1]:
                    res.append(mid)
                    return mid
                else:
                    low = mid + 1
            #if last ele is peak
            elif mid == len(nums) - 1:
                if nums[mid] > nums[mid-1]:
                    res.append(mid)
                    return mid
                else:
                    high = mid - 1
            else:
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    res.append(mid)
                    return mid
                # If the middle element < than its next element, means path is increasing path
                # and peak element is on the right side
                elif nums[mid] < nums[mid+1]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
    
res = [] #if the given array has multiple peaks
print(findPeakElement([1,2,3,1]))

print(findPeakElement([1,2,1,3,5,6,4]))
print(res)