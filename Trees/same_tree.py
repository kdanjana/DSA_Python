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
            if tree1 is None or tree2 is  None:#implies if tree1 is none and tree2 is not and viceversa , also cover case when both values are not same
                if tree1 == tree2:
                    return True
                else:
                    return False
            return tree1.val == tree2.val and dfs(tree1.left, tree2.left) and dfs(tree1.right, tree2.right)
        return dfs(p,q)