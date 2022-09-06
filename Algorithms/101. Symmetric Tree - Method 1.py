# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSym(root.left, root.right)
    
    def isSym(self, L, R):
        if L and R and L.val == R.val:
            return self.isSym(L.left, R.right) and self.isSym(L.right, R.left)
        return L == R
