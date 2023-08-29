class Solution {
    public int bestClosingTime(String customers) {
        char[] arr = customers.toCharArray();
        // Y 의 개수를 모두 세서 dp 에 저장
        // 다음 글자가 Y 라면 합계를 줄이고 N 이라면 합계를 늘린다.
        // 줄였을 때 최소값을 계속 확인
        int minPenalty = 0;
        int[] dp = new int[arr.length + 1];
        int minIdx = 0;
        for (char c : arr) {
            if (c == 'Y') {
                minPenalty++;
            }
        }
        dp[0] = minPenalty;
        
        for (int i = 1; i <= arr.length; i++) {
            if (arr[i - 1] == 'Y') {
                dp[i] = dp[i - 1] - 1;
            } else {
                dp[i] = dp[i - 1] + 1;
            }
            if (minPenalty > dp[i]) {
                minPenalty = dp[i];
                minIdx = i;
            }
        }

        return minIdx;
    }
}