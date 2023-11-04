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
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }

        return check(root, 1) != -1;
    }

    private int check(TreeNode root, int height) {
        if (root == null) {
            return height;
        }

        int left = check(root.left, 1);
        int right = check(root.right, 1);

        if (Math.abs(left - right) > 1) {
            return -1;
        }

        return Math.max(
            check(root.left, height + 1),
            check(root.right, height + 1)
        );
    }
}