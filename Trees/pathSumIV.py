""" 
The task is to find the sum of all root-to-leaf paths' values.
finding the sum of all paths in a binary tree represented in a list format.
The binary tree is represented by a list of integers where each integer contains three digits.
The first digit represents the depth d of the node, the second digit represents the position p 
of the node at that depth, and the third digit represents the value v of the node. For example, 
an integer 213 represents a node with a value of 3 located at depth 2, position 1.
A dictionary h is created to store the tree nodes in a more accessible format. 
The goal is to traverse the tree from the root to each leaf and accumulate the values of the nodes along these paths.
The keys are tuples representing the (depth, position) of each node, and the values are the node values.
curSum: The cumulative sum of node values along the current path.
depth: The current depth in the tree.
pos: The current position at that depth
"""


class Solution:
    def pathSum(self, nums: List[int]) -> int:
        h = {}
        for n in nums:
            depth = n//100
            pos = (n - depth*100)//10
            val = n % 10
            h[(depth-1, pos-1)] = val
        res = 0
        def dfs(curSum, depth, pos):
            nonlocal res
            val = h[(depth, pos)]
            left = (depth+1, pos*2)
            right = (depth+1, pos*2+1)
            if left in h and right in h:
                 dfs(curSum + val, depth+1, pos*2)
                 dfs(curSum + val, depth+1, pos*2+1)
            elif left in h:
                dfs(curSum + val, depth+1, pos*2)
            elif right in h:
                dfs(curSum + val, depth+1, pos*2+1)
            else:
                res += (curSum+val)
                return 
        dfs(0,0,0)
        return res
    
    
# another way 
""" 
The space complexity of the function is O(H), where H is the height of the binary tree represented by the nums array
The time complexity of the function is O(N), where N is the number of elements in the nums array. 
"""
def pathSum(self, nums: List[int]) -> int:
    # Helper function for depth-first search from a given node with cumulative total `total`
    def dfs(node, total):
        # If the current node is not in the tree, stop the recursion
        if node not in tree_map:
            return
        # Add the current node's value to the running total
        total += tree_map[node]
        depth, pos = divmod(node, 10) # Split the node code into depth and positional information
        # Calculate the node code for the left and right children
        left_child = (depth + 1) * 10 + (pos * 2) - 1
        right_child = left_child + 1
        # If both children are absent, add the current total to the global 'answer'
        if left_child not in tree_map and right_child not in tree_map:
            nonlocal answer
            answer += total
            return
        # Recurse on the left and right children
        dfs(left_child, total)
        dfs(right_child, total)
    # Initialize the answer variable to accumulate the total path sums
    answer = 0
    # Create a mapping from node codes (depth and position) to values using list comprehension
    tree_map = {num // 10: num % 10 for num in nums}
    #the DFS is kicked off from the root of the tree, which always has a depth and position of 1 (hence node 11), 
    # and an initial total path sum of 0
    dfs(11, 0)
    # Return the accumulated total path sums
    return answer