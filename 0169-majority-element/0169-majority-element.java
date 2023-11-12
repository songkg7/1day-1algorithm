class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> counter = new HashMap<>();
        int max = 0;
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            counter.put(nums[i], counter.getOrDefault(nums[i], 0) + 1);
            if (counter.get(nums[i]) > max) {
                ans = nums[i];
                max = counter.get(nums[i]);
            }
        }
        return ans;
    }
}