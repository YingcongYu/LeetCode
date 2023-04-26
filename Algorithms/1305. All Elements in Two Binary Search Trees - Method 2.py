# Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        output = []
        def traverse(root):
            if root:
                traverse(root.left)
                output.append(root.val)
                traverse(root.right)
        
        traverse(root1)
        traverse(root2)
        return sorted(output)
