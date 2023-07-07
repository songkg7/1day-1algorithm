class Solution {
    public int maxConsecutiveAnswers(String answerKey, int k) {
        // T 와 F 일 때 각각의 결과를 슬라이딩 윈도우로 찾는다
        // k 개만큼 윈도우 안에 상대 글자를 포함할 수 있다
        char[] arr = answerKey.toCharArray();
        int tCount = cal(arr, k, 'T');
        int fCount = cal(arr, k, 'F');
        return Math.max(tCount, fCount);
    }

    private int cal(char[] key, int k, char target) {
        int start = 0;
        int max = 0;
        int count = 0;
        for (int i = 0; i < key.length; i++) {
            if (key[i] != target) {
                count++;
            }
            while (count > k) {
                if (key[start++] != target) {
                    count--;
                }
            }
            max = Math.max(max, i - start + 1);
        }
        return max;
    }
}