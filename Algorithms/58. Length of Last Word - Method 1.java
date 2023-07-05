// Given a string s consisting of words and spaces, return the length of the last word in the string.

// A word is a maximal substring consisting of non-space characters only.


class Solution {
    public int lengthOfLastWord(String s) {
        String[] arr = s.split(" ", 0);
        return arr[arr.length-1].length();
    }
}
