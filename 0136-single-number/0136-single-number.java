import java.util.HashMap;
import java.util.Map;

class Solution {
    public int singleNumber(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            if (map.get(num) == null) {
                map.put(num, num);
            } else {
                map.remove(num);
            }
        }
        return map.keySet().stream().findFirst().orElseThrow();
    }
}