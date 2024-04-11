class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node == None:
                return None
            if node == p:
                return p
            if node == q:
                return q
            left_node = dfs(node.left)
            right_node = dfs(node.right)
            if left_node is None and right_node is not None: # right_node may be p or q 
                return right_node
            elif left_node is not None and right_node is None: # left_node may be p or q
                return left_node
            elif left_node is None and right_node is None: 
                return None
            elif left_node is not None and right_node is not None:
                return node
        return dfs(root)