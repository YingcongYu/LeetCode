# Given a binary tree, determine if it is height-balanced.
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, indicator):
            if not root:
                return 0
            
            l_level = dfs(root.left, indicator)
            r_level = dfs(root.right, indicator)
            if abs(r_level - l_level) > 1:
                indicator[0] = False
            return max(l_level, r_level) + 1
        
        indicator = [True]
        dfs(root, indicator)
        return indicator[0]
