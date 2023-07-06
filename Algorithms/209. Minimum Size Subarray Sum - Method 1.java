// Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. 
// If there is no such subarray, return 0 instead.


class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int output = Integer.MAX_VALUE;
        int cur_sum = 0;
        Deque<Integer> subarray = new ArrayDeque<>();

        for (int num : nums) {
            cur_sum += num;
            subarray.add(num);
            
            if (cur_sum >= target) {
                while (!subarray.isEmpty() && cur_sum-subarray.getFirst() >= target) {
                    cur_sum -= subarray.pollFirst();
                }
                output = Math.min(output, subarray.size());
            }
        }

        if (output != Integer.MAX_VALUE) {
            return output;
        }
        return 0;
    }
}
