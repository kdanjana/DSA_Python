""" 
You're given a sorted array 'a' of 'n' integers and an integer 'x'. Find the floor and ceiling of 'x' in 'a[0..n-1]'.
Floor of 'x' is the largest element in the array which is smaller than or equal to 'x'.
Ceiling of 'x' is the smallest element in the array greater than or equal to 'x'.
Input: 
n=6, x=5, a=[3, 4, 7, 8, 8, 10]   
The floor and ceiling of 'x' = 5 are 4 and 7, respectively.
"""


def getFloorAndCeil(a, x):
    # Write your code here.
    def getFloor(a,x):
        low = 0
        high = len(a) - 1
        mid = 0
        res = -1
        while low <= high:
            mid = low + ((high - low) // 2)
            if a[mid] <= x:
                res = a[mid]
                low = mid  + 1
            else:
                high = mid - 1
        return res
    def getCeil(a,x):
        res = -1
        low = 0
        high= len(a) - 1
        mid = 0
        while low <= high:
            mid = low + ((high- low ) // 2)
            if a[mid] >= x:
                res = a[mid]
                high = mid - 1
            else:
                low = mid + 1
        return res
    return getFloor(a,x), getCeil(a,x)


print(getFloorAndCeil([2, 3,9, 15, 21, 27, 28], 29))  # 28 -1