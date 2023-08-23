class Solution {
    public String reverseVowels(String s) {
        List<Character> vowels = List.of('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U');
        int start = 0;
        int end = s.length() - 1;

        char[] chars = s.toCharArray();

        while (start <= end) {
            if (vowels.contains(chars[start]) && vowels.contains(chars[end])) {
                char temp = chars[start];
                chars[start] = chars[end];
                chars[end] = temp;
                start++;
                end--;
                continue;
            }

            if (!vowels.contains(chars[start]) && vowels.contains(chars[end])) {
                start++;
            } else if (vowels.contains(chars[start]) && !vowels.contains(chars[end])) {
                end--;
            } else {
                start++;
                end--;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (char c : chars) {
            sb.append(c);
        }
        return sb.toString();
    }
}