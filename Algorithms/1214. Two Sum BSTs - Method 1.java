// Given the roots of two binary search trees, root1 and root2, return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.


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
    public boolean twoSumBSTs(TreeNode root1, TreeNode root2, int target) {
        HashSet<Integer> set1 = new HashSet<>();
        HashSet<Integer> set2 = new HashSet<>();

        Solution.dfs(root1, set1);
        Solution.dfs(root2, set2);

        for (Integer num:set1) {
            if (set2.contains(target - num)) {
                return true;
            }
        }
        return false;
    }

    public static void dfs(TreeNode root, HashSet input_set) {
        if (root != null) {
            input_set.add(root.val);
            dfs(root.left, input_set);
            dfs(root.right, input_set);
        }
    }
}
