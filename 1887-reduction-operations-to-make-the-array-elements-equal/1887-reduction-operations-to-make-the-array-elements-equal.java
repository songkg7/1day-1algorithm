class Solution {
    public int reductionOperations(int[] nums) {
        Arrays.sort(nums);
        int cnt = 0;
        int max = nums[nums.length - 1];
        int min = nums[0];

        List<Integer> changes = new ArrayList<>();
        for (int i = min + 1; i <= max; i++) {
            int foundValue = findFirst(nums, nums.length - 1, i);

            if (foundValue >= 0) {
                changes.add(foundValue);
            }
        }

        for (Integer index : changes) {
            cnt += nums.length - index;
        }

        return cnt;
    }

    private int findFirst(int[] nums, int currentIndex, int key) {
        if (currentIndex < 0) {
            return -1;
        }
        int foundValue = Arrays.binarySearch(nums, 0, currentIndex + 1, key);
        if (foundValue == currentIndex) {
            return currentIndex;
        }
        return findFirst(nums, foundValue, key);
    }

}