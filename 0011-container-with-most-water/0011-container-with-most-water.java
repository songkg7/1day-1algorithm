class Solution {
    public int maxArea(int[] height) {
        // 두 포인터의 index 차이가 x, 두 포인터의 높이 중 낮은 값이 y
        // x * y = amount of water
        int left = 0;
        int right = height.length - 1;
        int max = 0;

        // Until left and right become the same
        while (left < right) {
            int heightOfWater = Math.min(height[left], height[right]);
            System.out.println(heightOfWater);
            max = Math.max(heightOfWater * (right - left), max);

            if (height[left] > height[right]) {
                right--;
            } else {
                left++;
            }
        }

        return max;
    }
}