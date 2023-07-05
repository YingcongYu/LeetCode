// Given a string s consisting of words and spaces, return the length of the last word in the string.

// A word is a maximal substring consisting of non-space characters only.


class Solution {
    public int lengthOfLastWord(String s) {
        int last_letter = s.length() - 1;
        while (s.charAt(last_letter) == ' ') {
            last_letter--;
        }

        int first_letter = last_letter;
        while (first_letter >= 0 && s.charAt(first_letter) != ' ') {
            first_letter--;
        }

        return last_letter - first_letter;
    }
}
