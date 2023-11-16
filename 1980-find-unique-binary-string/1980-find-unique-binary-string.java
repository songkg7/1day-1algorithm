class Solution {
    public String findDifferentBinaryString(String[] nums) {
        int[] array = new int[(int) Math.pow(2, nums.length)];
        for (String s : nums) {
            int i = Integer.parseInt(s, 2);
            array[i] = 1;
        }
        String ans = "";
        for (int i = 0; i < array.length; i++) {
            if (array[i] == 0) {
                ans += Integer.toBinaryString(i);
                break;
            }
        }
        int zeroCount = nums.length - ans.length();
        String zero = "0".repeat(zeroCount);
        return zero + ans;
    }
}