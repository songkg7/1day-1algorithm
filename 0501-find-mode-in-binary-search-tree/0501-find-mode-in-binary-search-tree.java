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
    public int[] findMode(TreeNode root) {
        // Map 을 하나 주고, key 가 이미 존재하면 value + 1
        // 가장 큰 value 를 가진 key 를 반환
        Map<Integer, Integer> counter = new HashMap<>();
        dfs(root, counter);
        int max = 0;
        for (int key : counter.keySet()) {
            max = Math.max(max, counter.get(key));
        }

        List<Integer> result = new ArrayList();
        for (int key : counter.keySet()) {
            if (counter.get(key) == max) {
                result.add(key);
            }
        }

        int[] ans = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            ans[i] = result.get(i);
        }

        return ans;
    }

    public void dfs(TreeNode node, Map<Integer, Integer> counter) {
        if (node == null) {
            return;
        }

        counter.put(node.val, counter.getOrDefault(node.val, 0) + 1);
        dfs(node.left, counter);
        dfs(node.right, counter);
    }
}