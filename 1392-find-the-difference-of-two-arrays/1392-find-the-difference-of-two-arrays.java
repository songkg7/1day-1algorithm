class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        for (int num : nums1) {
            set1.add(num);
        }
        Set<Integer> set2 = new HashSet<>();
        for (int num : nums2) {
            set2.add(num);
        }

        var os1 = new HashSet<>(set1);
        var os2 = new HashSet<>(set2);

        List<List<Integer>> ans = new ArrayList<>();
        os1.removeAll(set2);
        os2.removeAll(set1);

        ans.add(os1.stream().toList());
        ans.add(os2.stream().toList());

        return ans;
    }
}