# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal and len(s) > len(set(s)):
            return True

        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append([s[i], goal[i]])
                if len(diff) > 2:
                    return False

        if len(diff) == 2 and diff[0] == diff[1][::-1]:
            return True
        return False
