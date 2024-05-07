""" 
Given the root of a binary tree, the value of a target node target, and an integer k, 
return an array of the values of all nodes that have a distance k from the target node.
intution::
To solve this problem, we need to find all nodes that are at the specified distance k 
from the target node, regardless of whether they're ancestors, descendants, or neither 
(siblings or cousins).  
We first need a way to traverse the tree not only downwards from the root to the leaves
(as is normally the case with tree traversals) but also upwards, from any node to its 
parent. This is not usually possible in a binary tree because nodes don't have a reference
to their parent. Therefore, we create a map that keeps track of each node's parent
Once we have the ability to move both up and down the tree, we perform a depth-first search
(DFS) starting from the target node. As we explore the tree, we keep track of the current 
distance from the target. When this distance equals k, we add the current node's value to 
our answer.
To ensure we don't count any nodes twice or enter a loop, we keep a set of visited nodes.
Whenever we visit a node, we add it to the set. If we encounter a node that's already 
in our set, we skip it.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # keys are nodes of the tree and values are their respective parent nodes
        nodeParents = {}
        def mappingParents(node, prev_node):
            nonlocal nodeParents
            if node is None:
                return
            nodeParents[node] = prev_node
            mappingParents(node.left, node)
            mappingParents(node.right, node)
        mappingParents(root,None)

        #perform a depth-first search, starting from the target node to
        # find nodes at distance k
        def findNodes(node, curr_distance):
            if node is  None or node.val in visited:
                return 
            visited.add(node.val)
            if curr_distance == 0:
                res.append(node.val)
            else:
                findNodes(node.left, curr_distance-1)
                findNodes(node.right, curr_distance-1)
                findNodes(nodeParents[node] , curr_distance-1)
        
        visited = set()
        res = []
        findNodes(target, k)
        return res


