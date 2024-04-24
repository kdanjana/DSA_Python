""" 
Given a binary tree, the task is to find the maximum path sum. 
The path may start and end at any node in the tree.
"""


class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        #Your code here
        def dfs(root):
            if not root:
                return 0
            leftpath_sum = max(0,dfs(root.left))
            rightpath_sum = max(0,dfs(root.right))
            self.res = max(self.res, root.data+leftpath_sum+rightpath_sum)
            return root.data+max(leftpath_sum, rightpath_sum)
        self.res = float('-inf')
        dfs(root)
        return self.res
    
    
import sys
from collections import deque

#function to build tree
def buildTree(s):
    if len(s) == 0 or s[0] == "N":
        return None
    #creating list of stringd from input string after splitting by space
    ip = list(map(str,s.split()))
    #create root of tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()
    #push root to q
    q.append(root)
    size += 1
    i = 1 # starting from second ele
    while  size > 0 and i < len(ip):
        curr_node = q[0]
        q.popleft()
        size -= 1
        curr_val = ip[i]
         # for left child
        if curr_val != "N":
            curr_node.left = Node(int(curr_val))
            q.append(curr_node.left)
            size += 1
        i += 1
        if i >= len(ip):
            break
        curr_val = ip[i]
        # for right child
        if curr_val != "N":
            curr_node.right = Node(int(curr_val))
            q.append(curr_node.right)
            size += 1
        i += 1
    return root

if __name__ == "__main__":
    root = buildTree(input())
    ob = Solution()
    print(ob.findMaxSum(root))
        
    
