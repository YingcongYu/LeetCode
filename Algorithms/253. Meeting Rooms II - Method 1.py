# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ref = [intervals[0]]
        for i in intervals[1:]:
            flag = 0
            for j in range(len(ref)):
                if i[0] >= ref[j][1]:
                    ref[j] = i
                    flag = 1
                    break
            if flag == 0:
                ref.append(i)
        return len(ref)
