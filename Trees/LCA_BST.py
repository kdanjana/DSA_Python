class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node is None:
                return None
            if node.val < p.val and node.val < q.val :
                return dfs(node.right)
            if node.val > p.val and node.val > q.val:
                return dfs(node.left)
            return node
        return dfs(root) 