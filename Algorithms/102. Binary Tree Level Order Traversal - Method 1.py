# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, level, output):
            if root:
                if len(output) <= level:
                    output.append([root.val])
                else:
                    output[level].append(root.val)
                dfs(root.left, level+1, output)
                dfs(root.right, level+1, output)
        
        level = 0
        output = []
        dfs(root, level, output)
        return output
