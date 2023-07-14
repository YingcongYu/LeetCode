// Given an integer array arr and an integer difference, 
// return the length of the longest subsequence in arr which is an arithmetic sequence 
//   such that the difference between adjacent elements in the subsequence equals difference.

// A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.


class Solution {
    public int longestSubsequence(int[] arr, int difference) {
        Map<Integer, Integer> visited = new HashMap<>();
        int output = 1;

        for (int i = arr.length-1; i >= 0; i--) {
            if (visited.containsKey(arr[i]+difference)) {
                visited.put(arr[i], visited.get(arr[i]+difference)+1);
                output = Math.max(output, visited.get(arr[i]));
            }
            else {
                visited.put(arr[i], 1);
            }
        }

        return output;
    }
}
