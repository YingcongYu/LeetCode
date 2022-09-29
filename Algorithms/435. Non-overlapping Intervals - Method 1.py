# Given an array of intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sort = sorted(intervals, key = lambda x: (x[1], x[0]))
        start = list(zip(*sort))[0]
        end = list(zip(*sort))[1]
        i = 0
        need = 1
        length = len(start)
        for j in range(1, length):
            if end[i] <= start[j]:
                need += 1
                i = j
        return length - need
