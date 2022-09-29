# Given an array of intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        output = 0
        pre_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= pre_end:
                pre_end = end
            else:
                output += 1
        return output
