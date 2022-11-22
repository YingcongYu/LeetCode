# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def postorder(root):
            if not root:
                return 0
            l_depth = postorder(root.left)
            r_depth = postorder(root.right)
            self.max_diameter = max(self.max_diameter, l_depth + r_depth)
            return max(l_depth, r_depth) + 1
        
        self.max_diameter = 0
        postorder(root)
        return self.max_diameter
