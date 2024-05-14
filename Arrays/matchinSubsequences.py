""" 
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace"

"""
" https://www.youtube.com/watch?v=Vch3pFgmKD8 "
from collections import defaultdict, deque


def numMatchingSubseq(s, words):
    #key - characters present in s and all word's in words array
    # value - array of strings which starts with key and ends until end of word in words
    d = defaultdict(deque)
    for w in words:
        d[w[0]].append(w)
    ans = 0
    print(d)
    for c in s:
        print(c, d[c])
        for _ in range(len(d[c])):
            t = d[c].popleft()
            if len(t) == 1:
                ans += 1
            else:
                d[t[1]].append(t[1:])
        print(d)
    return ans
    
print("res is ", numMatchingSubseq("abcde",["a","bb","acd","ace", "adk"]))