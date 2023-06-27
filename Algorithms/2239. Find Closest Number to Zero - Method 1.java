// Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.


class Solution {
    public int findClosestNumber(int[] nums) {
        int output = nums[0];
        for (int n:nums) {
            if (Math.abs(output) > Math.abs(n)) {
                output = n;
            }
            else if (Math.abs(output) == Math.abs(n)) {
                output = Math.max(output, n);
            }
        }
        return output;
    }
}
