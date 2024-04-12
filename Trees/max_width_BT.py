class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #use bfs or level order traversal
        max_width = 0
        # Queue will hold tuples of tree node and its index in the tree
        q = deque([(root, 1)])
        while len(q) != 0:
            # Calculate the current width using the first and last node's indices
            current_width = q[-1][1] - q[0][1] + 1
            max_width = max(max_width, current_width)  
            # Iterate over the current level of the tree
            for _ in range(len(q)):
                node, index = q.popleft()
                if node.left:
                    q.append((node.left, 2 * index))
                if node.right:
                    q.append((node.right, (2 * index) + 1))

        return max_width