// Given the root of a binary tree, return the number of uni-value subtrees.

// A uni-value subtree means all nodes of the subtree have the same value.


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
    int output = 0;

    public int countUnivalSubtrees(TreeNode root) {
        dfs(root);
        return output;
    }

    public boolean dfs(TreeNode root) {
        if (root != null) {
            boolean left = dfs(root.left);
            boolean right = dfs(root.right);

            if (left && right) {
                if (root.left != null && root.left.val != root.val) {
                    return false;
                }
                if (root.right != null && root.right.val != root.val) {
                    return false;
                }
                output++;
                return true;
            }
            return false;
        }
        return true;
    }
}
