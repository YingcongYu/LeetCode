// Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

// Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

// For example, swapping at indices 0 and 2 in "abcd" results in "cbad".


class Solution {
    public boolean buddyStrings(String s, String goal) {
        if (s.length() != goal.length()) {
            return false;
        }
        
        if (s.equals(goal)) {
            int[] frequency = new int[26];
            for (char ch : s.toCharArray()) {
                frequency[ch - 'a'] += 1;
                if (frequency[ch - 'a'] == 2) {
                    return true;
                }
            }
        }

        ArrayList<ArrayList<Character>> diff = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != goal.charAt(i)) {
                if (diff.size() > 0) {
                    diff.add(new ArrayList<>(Arrays.asList(goal.charAt(i), s.charAt(i))));
                }
                else if (diff.size() > 2){
                    return false;
                }
                else {
                    diff.add(new ArrayList<>(Arrays.asList(s.charAt(i), goal.charAt(i))));
                }
            }
        }

        if (diff.size() == 2 && diff.get(0).equals(diff.get(1))) {
            return true;
        }
        return false;
    }
}
