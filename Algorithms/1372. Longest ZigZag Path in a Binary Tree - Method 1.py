# You are given the root of a binary tree.

# A ZigZag path for a binary tree is defined as follow:

# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

# Return the longest ZigZag path contained in that tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def track(root, pre, cur):
            if not root:
                output[0] = max(output[0], cur)
                return
            if pre == 'left':
                track(root.right, 'right', cur+1)
                track(root.left, 'left', 0)
            else:
                track(root.left, 'left', cur+1)
                track(root.right, 'right', 0)
        
        output = [0]
        track(root.left, 'left', 0)
        track(root.right, 'right', 0)
        return output[0]
