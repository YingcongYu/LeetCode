// Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. 
// If there is no such subarray, return 0 instead.


class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int output = Integer.MAX_VALUE;
        int cur_sum = 0;
        int left = 0;

        for (int right = 0; right < nums.length; right++) {
            cur_sum += nums[right];

            while (cur_sum >= target) {
                output = Math.min(output, right - left + 1);
                cur_sum -= nums[left];
                left++;
            }
        }

        if (output == Integer.MAX_VALUE) {
            return 0;
        }
        return output;
    }
}
