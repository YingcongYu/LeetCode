###Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return mode(arr)
