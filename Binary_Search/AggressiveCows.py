""" 
You are given an array consisting of n integers which denote the position of a stall. 
You are also given an integer k which denotes the number of aggressive cows. You are given the task of 
assigning stalls to k cows such that the minimum distance between any two of them is the maximum possible

"""


def solve(self,n,k,stalls):
        # can we place all cows at stall positions with minimu distance between them distance
        def canWePlace(distance):
            #cow is placed stall index 0
            lastStall = stalls[0]
            # one cow is already placed at first stall
            cowCount = 1
            for i in range(1,len(stalls)):
                if stalls[i] - lastStall >= distance:
                    cowCount += 1
                    lastStall = stalls[i]
                    if cowCount == k:
                        return True
            return False
        
        stalls.sort()
        #minimum distance between stalls of 2 cows
        low = 1
        #maximum distance between stalls of 2 cows
        high = stalls[-1] - stalls[0]
        res = -1
        while low <= high:
            mid = low + ((high-low) // 2)
            if canWePlace(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res
    
    
    
print(solve([1, 2, 4, 8, 9], 3))