class Solution {
    public boolean repeatedSubstringPattern(String s) {
        String answer = "";
        for (int i = 1; i < s.length() / 2 + 1; i++) {
            answer = s.substring(0, i);
            if (answer.repeat(s.length() / i).equals(s)) {
                return true;
            }
        }
        return false;
    }
}