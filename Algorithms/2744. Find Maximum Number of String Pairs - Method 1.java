// You are given a 0-indexed array words consisting of distinct strings.

// The string words[i] can be paired with the string words[j] if:

// The string words[i] is equal to the reversed string of words[j].
// 0 <= i < j < words.length.
// Return the maximum number of pairs that can be formed from the array words.

// Note that each string can belong in at most one pair.


class Solution {
    public int maximumNumberOfStringPairs(String[] words) {
        Map<String,Integer> ref = new HashMap<>();
        for (String s:words) {
            String rev = new StringBuilder(s).reverse().toString();
            if (ref.containsKey(rev)) {
                ref.put(rev, ref.get(rev)+1);
            }
            else {
                ref.put(s, 0);
            }
        }

        int output = 0;
        for (int n:ref.values()) {
            output += n;
        }
        
        return output;
    }
}
