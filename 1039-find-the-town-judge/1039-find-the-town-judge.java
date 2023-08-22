class Solution {
    public int findJudge(int n, int[][] trust) {
        if (trust.length == 0 && n == 1) {
            return 1;
        }
        int[] count = new int[n + 1];
        for (int[] person : trust) {
            count[person[0]]--;
            count[person[1]]++;
        }

        for (int person = 1; person < count.length; person++) {
            // 본인을 제외한 모두의 신뢰를 얻는다면
            if (count[person] == n - 1) {
                return person;
            }
        }
        return -1;
    }
}