# Given the root of a binary tree, return the sum of values of its deepest leaves.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        nodes = [root]
        pre = 0

        while nodes:
            temp = []
            cur = 0
            for i in nodes:
                if i:
                    cur += i.val
                    temp.append(i.left)
                    temp.append(i.right)
            if not temp:
                return pre
            nodes = temp
            pre = cur
