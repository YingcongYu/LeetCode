# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        l = [root]
        while l:
            check = [i.val if i else None for i in l]
            if check != check[::-1]:
                return False
            l = [x for i in l if i for x in [i.left, i.right]]
        return True
