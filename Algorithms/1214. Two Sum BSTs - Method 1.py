# Given the roots of two binary search trees, root1 and root2, return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def dfs(root, input_set):
            if not root:
                return
            input_set.add(root.val)
            if root.right:
                dfs(root.right, input_set)
            if root.left:
                dfs(root.left, input_set)
        
        set1 = set()
        dfs(root1, set1)
        set2 = set()
        dfs(root2, set2)

        for i in set1:
            if target - i in set2:
                return True     
        return False
