# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if root:
                inorder(root.left)
                self.kth += 1
                if self.kth == k:
                    self.mark = root.val
                inorder(root.right)
            
        self.kth = 0
        self.mark = None
        inorder(root)
        return self.mark
