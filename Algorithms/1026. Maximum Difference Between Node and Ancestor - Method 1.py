# Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, max_val, min_val):
            if not root:
                output[0] = max(output[0], max_val - min_val)
                return
            dfs(root.left, max(max_val, root.val), min(min_val, root.val))
            dfs(root.right, max(max_val, root.val), min(min_val, root.val))
        
        output = [0]
        dfs(root, root.val, root.val)
        return output[0]
