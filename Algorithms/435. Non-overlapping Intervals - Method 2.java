// Given an array of intervals intervals where intervals[i] = [starti, endi], 
// return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.


class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));
        int output = 0;
        int pre_end = Integer.MIN_VALUE;

        for (int i = 0; i < intervals.length; i++) {
            if (intervals[i][0] >= pre_end) {
                pre_end = intervals[i][1];
            }
            else {
                output++;
            }
        }

        return output;
    }
}
