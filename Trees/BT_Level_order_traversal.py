class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        
        q = []
        q.append(root)
        
        while len(q) != 0:
            # level size
            curr_len = len(q)
            # current level nodes
            level_res = []
            while curr_len != 0:
                curr_node = q.pop(0)
                level_res.append(curr_node.val)
                if curr_node.left is not None:
                    q.append(curr_node.left)
                if curr_node.right is not None:
                    q.append(curr_node.right)
                curr_len -= 1
            res.append(level_res)
        
        return res