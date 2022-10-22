# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: (x[0], x[1]))
        output = [intervals[0]]
        for i in intervals[1:]:
            if i[0] <= output[-1][1]:
                if i[1] > output[-1][1]:
                    output[-1] = [output[-1][0], i[1]]
                else:
                    continue
            else:
                output.append(i)
        return output
