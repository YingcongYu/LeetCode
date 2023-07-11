// Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

// You can return the answer in any order.


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    Map<TreeNode, TreeNode> parents = new HashMap<>();
    List<Integer> output = new ArrayList<>();
    Set<TreeNode> visited = new HashSet<>();

    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        add_parent(root);

        List<TreeNode> nodes = new ArrayList<>();
        nodes.add(root);
        while (!nodes.isEmpty()) {
            List<TreeNode> temp = new ArrayList<>();
            for (TreeNode node : nodes) {
                if (node == null) {
                    continue;
                }

                if (node.val == target.val) {
                    dfs(node, k);
                    temp.clear();
                    break;
                }

                temp.add(node.left);
                temp.add(node.right);
            }

            nodes = temp;
        }

        return output;
    }

    public void add_parent(TreeNode cur) {
        if (cur != null) {
            if (cur.left != null) {
                parents.put(cur.left, cur);
                add_parent(cur.left);
            }
            if (cur.right != null) {
                parents.put(cur.right, cur);
                add_parent(cur.right);
            }
        }
    }

    public void dfs(TreeNode cur, int k) {
        if (cur == null) {
            return;
        }

        if (visited.contains(cur)) {
            return;
        }

        if (k == 0) {
            output.add(cur.val);
            return;
        }

        visited.add(cur);
        if (cur.left != null) {
            dfs(cur.left, k-1);
        }
        if (cur.right != null) {
            dfs(cur.right, k-1);
        }
        dfs(parents.get(cur), k-1);
        return;
    }
}
