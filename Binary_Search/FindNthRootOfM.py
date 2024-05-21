""" 
You are given 2 numbers (n , m); the task is to find n√m (nth root of m).
Input: n = 3, m = 9
Output: -1
Explanation: 3rd root of 9 is not integer
Input: n = 2, m = 9
Output: 3
Explanation: 32 = 9
"""


def NthRoot(n, m):
    low = 1
    high = m
    while low <= high:
        mid = low + ((high-low)//2)
        val = pow(mid,n)
        print(low, high, mid, val)
        if val == m:
            return mid
        elif val < m:
            print("right")
            low = mid + 1
        else:
            print("left")
            high = mid - 1
    return -1

print(NthRoot(2,9))
print(NthRoot(3,9))