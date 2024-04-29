""" 
A well-known approach to creating a balanced BST is to first convert the BST
into a sorted array and then to rebuild the BST from this array.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        #function to perform inorder traversal and collect values in a list.
        def inorder_traversal(node):
            if node is None: 
                return
            inorder_traversal(node.left)  # Recurse on left subtree.
            node_values.append(node.val)  # Append the value of the current node.
            inorder_traversal(node.right)  # Recurse on right subtree.

        # function to build a balanced BSTfrom  given  sorted value list.
        def build_balanced_bst(start, end):
            if start > end:  
                return None
            mid = (start + end) // 2  
            node = TreeNode(node_values[mid]) 
            # Recursively build left and right subtrees using the split lists.
            node.left = build_balanced_bst(start, mid - 1)
            node.right = build_balanced_bst(mid + 1, end)
            return node  # Return the newly created node.

        node_values = []  # Initialize an empty list to store the tree node values.
        inorder_traversal(root)  # Fill the node_values list with values from the BST.
        # Build and return a balanced BST using the list of values.
        return build_balanced_bst(0, len(node_values) - 1)