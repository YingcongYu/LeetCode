# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_root = TreeNode()

        def preorder(root, new_root):
            if not root:
                return
            if root.val == val:
                new_root.left = root
            preorder(root.left, new_root)
            preorder(root.right, new_root)
        
        preorder(root, new_root)
        return new_root.left
