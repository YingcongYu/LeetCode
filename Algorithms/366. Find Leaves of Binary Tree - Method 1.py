# Given the root of a binary tree, collect a tree's nodes as if you were doing this:

# Collect all the leaf nodes.
# Remove all the leaf nodes.
# Repeat until the tree is empty.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, pre, direction):
            if not root.left and not root.right:
                temp.append(root.val)
                if direction == 'l':
                    pre.left = None
                else:
                    pre.right = None
            else:
                if root.left:
                    dfs(root.left, root, 'l')
                if root.right:
                    dfs(root.right, root, 'r')
        
        output = []
        while root.left or root.right:
            temp = []
            if root.left:
                    dfs(root.left, root, 'l')
            if root.right:
                dfs(root.right, root, 'r')
            output.append(temp)
        
        output.append([root.val])
        return output
