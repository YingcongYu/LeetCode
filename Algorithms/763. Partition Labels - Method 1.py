# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        window = {}
        for i in set(s):
            window[i] = [s.find(i), s.rfind(i)]

        output = []
        left = window[s[0]][0]
        right = window[s[0]][1]
        for i in s:
            if window[i]:
                if window[i][1] > right:
                    if window[i][0] > right:
                        output.append(right-left+1)
                        left = window[i][0]
                    right = window[i][1]
                window[i] = []

        output.append(right-left+1)
        return output
