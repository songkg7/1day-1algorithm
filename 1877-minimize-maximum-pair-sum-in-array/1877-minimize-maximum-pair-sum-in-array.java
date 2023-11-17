class Solution {
    public int minPairSum(int[] nums) {
        // 모든 페어는 최대한 작은 숫자를 가져야 한다.
        // 가장 큰 수는 가장 작은 수와 페어를 이뤄야 한다.
        // nums 를 정렬 후 양쪽 끝에서 안쪽으로 페어를 이루게 한다.
        // 그 과정에서 최대값을 기억해뒀다가 반환한다.
        Arrays.sort(nums);
        int max = 0;
        int start = 0;
        int end = nums.length - 1;

        while (start < end) {
            int sum = nums[start++] + nums[end--];
            max = Math.max(max, sum);
        }

        return max;
    }
}