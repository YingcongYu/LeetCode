# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

# You can return the answer in any order.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def add_parent(cur, parent):
            if cur:
                cur.parent = parent
                add_parent(cur.left, cur)
                add_parent(cur.right, cur)
        
        add_parent(root, None)
        output = []
        visited = set()

        def dfs(cur, path):
            if not cur or cur in visited:
                return
            
            visited.add(cur)
            
            if path == 0:
                output.append(cur.val)
                return
            
            dfs(cur.parent, path - 1)
            dfs(cur.left, path - 1)
            dfs(cur.right, path - 1)
        
        dfs(target, k)

        return output
