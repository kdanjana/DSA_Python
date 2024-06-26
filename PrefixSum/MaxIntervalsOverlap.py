""" 
Consider a big party where N guests came to it and a log register for guest’s entry and exit times was
maintained. Find the minimum time at which there were maximum guests at the party. Note that entries in 
the register are not in any order. 
Note: Guests are leaving after the exit times
Input:
N = 7
Entry= {13, 28, 29, 14, 40, 17, 3}
Exit = {107, 95, 111, 105, 70, 127, 74}
Output: 7 40
Explanation: At time 40 there were 
             all 7 guests present in the party.

"""

from collections import Counter
from itertools import accumulate

class Solution:

    def findMaxGuests(self, Entry, Exit, N):
        Entry.sort()
        Exit.sort()
        MaxGuests = 0
        guestsIn = 0
        time = 0
        i = 0
        j = 0
        while i < N:
            if Entry[i] <= Exit[j]:
                guestsIn += 1
                if guestsIn > MaxGuests:
                    MaxGuests = guestsIn
                    time = Entry[i]
                i += 1
            else:
                guestsIn -= 1
                j += 1
        return MaxGuests, time

if __name__ == "__main__":
    entryTimes = [int(x) for x in input().split(',')]
    exitTimes = [int(x) for x in input().split(',')]
    solu = Solution()
    ans = solu.findMaxGuests(entryTimes, exitTimes)
    print(ans[0], ans[1])