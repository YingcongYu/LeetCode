# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
# Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []
        path = []
        curSum = 0
        
        def dfs(node, curSum):
            if not node:
                return
            
            curSum += node.val
            path.append(node.val)
            
            if not node.left and not node.right and curSum == targetSum:
                output.append(path[:])
                curSum -= node.val
                path.pop()
                return
            
            dfs(node.left, curSum)
            dfs(node.right, curSum)
            path.pop()
            curSum -= node.val
        
        dfs(root, curSum)
        
        return output
