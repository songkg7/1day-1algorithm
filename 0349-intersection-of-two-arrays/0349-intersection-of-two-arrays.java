import java.util.Arrays;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        
        Set<Integer> set = new HashSet<>();
        for (int num : nums1) {
            if (Arrays.binarySearch(nums2, num) >= 0) {
                set.add(num);
            }
        }
        return set.stream().mapToInt(Integer::intValue).toArray();
    }
}