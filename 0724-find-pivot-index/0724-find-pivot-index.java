class Solution {
    public int pivotIndex(int[] nums) {
        int left = 0;
        int right = 0;
        for (int num : nums) {
            right += num;
        }

        for (int pivot = 0; pivot < nums.length; pivot++) {
            if (pivot == 0) {
                right -= nums[pivot];    
            } else if (pivot == nums.length - 1) {
                right = 0;
                left += nums[pivot - 1];
            } else {
                left += nums[pivot - 1];
                right -= nums[pivot];
            }
            if (left == right) {
                return pivot;
            }
        }

        return -1;
    }
}