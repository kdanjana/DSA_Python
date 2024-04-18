#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import Counter


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # get all the subtrees of given tree, for that u need to traverse tree we are using
        # pre-order traversal to serialize each subtree
        
        def traverse(node):
            # Returns: A string representing the serialized form of the subtree rooted at the current node.
            if node is None:
                return 'null'
            serialized_subtree = f'{node.val},{traverse(node.left)},{traverse(node.right)}'
            subtree_counter[serialized_subtree] += 1
            if subtree_counter[serialized_subtree] == 2:
                duplicate_subtrees.append(node)
            return serialized_subtree

        # List to hold the root nodes of duplicate subtrees
        duplicate_subtrees = []
        # Counter to track the number of times a serialized subtree occurs
        subtree_counter = Counter()
        traverse(root)
        print(subtree_counter)
        return duplicate_subtrees
            
            
        