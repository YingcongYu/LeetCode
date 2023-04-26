# Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        nodes = [root1, root2]
        output = []

        while nodes:
            temp = nodes.pop(0)
            if temp:
                output.append(temp.val)
                if temp.left:
                    nodes.append(temp.left)
                if temp.right:
                    nodes.append(temp.right)
        
        return sorted(output)
