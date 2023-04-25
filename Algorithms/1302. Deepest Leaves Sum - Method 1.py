# Given the root of a binary tree, return the sum of values of its deepest leaves.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ref = collections.defaultdict(list)

        def dfs(root, level):
            if root:
                ref[level].append(root.val)
                dfs(root.left, level+1)
                dfs(root.right, level+1)
        
        dfs(root, 1)
        return sum(ref[max(ref)])
