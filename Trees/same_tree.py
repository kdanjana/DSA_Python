""" 
Given the roots of two binary trees p and q, write a function to check if they are the 
same or not. Two binary trees are considered the same if they are structurally identical, 
and the nodes have the same value."""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(tree1, tree2):
            if tree1 is None and tree2 is None:
                return True
            if (tree1 is None and tree2 is not None) or (tree1 is not None and tree2 is None):
                return False
            #tree1 and tree2 not empty
            return tree1.val == tree2.val and dfs(tree1.left, tree2.left) and dfs(tree1.right, tree2.right)
        return dfs(p,q)