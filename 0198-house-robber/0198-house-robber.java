import java.lang.Math;

class Solution {
    public int rob(int[] nums) {
        if (nums.length < 3) {
            return nums.length == 2 ? Math.max(nums[0], nums[1]) : nums[0];
        }

        int[] dp = new int[nums.length];
        int len = dp.length;
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);
        dp[2] = nums[2] + nums[0];
        for (int i = 3; i < nums.length; i++) {
            dp[i] = nums[i] + Math.max(dp[i - 2], dp[i - 3]);
        }
        return Math.max(dp[len - 2], dp[len - 1]);
    }
}