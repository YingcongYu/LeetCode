# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        output = []
        all_nodes = self.inorder(root, output)
        index = 1
        while index < len(all_nodes):
            if all_nodes[index-1] >= all_nodes[index]:
                return False
            index += 1
        return True
        
    def inorder(self, root, output):
        if root:
            output = self.inorder(root.left, output)
            output.append(root.val)
            output = self.inorder(root.right, output)
        return output
