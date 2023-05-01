# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        window = {}
        for i in range(len(s)):
            if s[i] in window:
                window[s[i]][1] = i
            else:
                window[s[i]] = [i, i]

        output = []
        ref = list(window.values())
        ref.sort(key = lambda x: x[0])
        left = ref[0][0]
        right = ref[0][1]
        for i in ref[1:]:
            if i[1] > right:
                if i[0] > right:
                    output.append(right-left+1)
                    left = i[0]
                right = i[1]

        output.append(right-left+1)
        return output
