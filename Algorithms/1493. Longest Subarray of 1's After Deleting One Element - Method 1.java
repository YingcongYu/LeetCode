// Given a binary array nums, you should delete one element from it.

// Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.


class Solution {
    public int longestSubarray(int[] nums) {
        int output = 0;
        int cur = 0;
        int pre = 0;

        for (int num : nums) {
            if (num == 1) {
                cur += 1;
            }
            else {
                output = Math.max(output, pre+cur);
                pre = cur;
                cur = 0;
            }
        }
        
        output = Math.max(output, pre+cur);
        if (cur == nums.length) {
            output--;
        }
        return output;
    }
}
