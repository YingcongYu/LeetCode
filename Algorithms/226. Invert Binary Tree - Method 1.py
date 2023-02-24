# Given the root of a binary tree, invert the tree, and return its root.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        def bfs(root):
            if not root:
                return
            
            temp = root.left
            root.left = root.right
            root.right = temp
            bfs(root.left)
            bfs(root.right)
            
        bfs(root)
        return root
