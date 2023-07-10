// Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.


class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        int end = 0;
        int output = 0;
        Map<Character, Integer> letters = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            Character temp = s.charAt(i);
            letters.put(temp, letters.get(temp)==null ? 1 : letters.get(temp)+1);
            while (letters.size() > k) {
                temp = s.charAt(end);
                if (letters.get(temp) == 1) {
                    letters.remove(temp);
                }
                else {
                    letters.put(temp, letters.get(temp)-1);
                }
                end++;
            }

            output = Math.max(output, i - end + 1);
        }

        return output;
    }
}
