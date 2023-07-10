// Given a binary tree, find its minimum depth.

// The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

// Note: A leaf is a node with no children.


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int output = Integer.MAX_VALUE;

    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        dfs(root, 1);

        return output;
    }

    public void dfs(TreeNode root, int path) {
        if (root.left == null && root.right == null) {
            output = Math.min(output, path);
            return;
        }

        if (root.left != null) {
            dfs(root.left, path+1);
        }
        if (root.right != null) {
            dfs(root.right, path+1);
        }
    }
}
