# given a BT find all the subtrees,
# we are using preorder tarversal

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# dfs , preorder tarfersal
def traverse(node, subtree_counts):
    if not node:
        return "#"
    # Serialize the subtree whose root is 'node'
    root_val = str(node.value)
    left_val = "#" if (node.left is None and node.right is not None) else traverse(node.left, subtree_counts)
    right_val = "#" if (node.right is None  and node.left is not None) else traverse(node.right, subtree_counts)
    subtree_str = f'[{root_val},{left_val},{right_val}]'
    # Update the counts 
    subtree_counts[subtree_str] = subtree_counts.get(subtree_str,0) + 1
    return subtree_str
    

# Driver code
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(2)
    root.right.right.left = TreeNode(4)
    root.right.right.right = TreeNode(3)
    # Dictionary to store subtree string representations and their counts
    subtree_counts = {}
    traverse(root, subtree_counts)
    print(subtree_counts)
    for subtree, count in subtree_counts.items():
        print(subtree)
