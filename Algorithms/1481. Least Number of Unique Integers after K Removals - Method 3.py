# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        ref = collections.Counter(arr)
        counts = collections.Counter(ref.values())
        output = len(ref)

        for i in range(1, len(arr)+1):
            if k >= i * counts[i]:
                k -= i * counts[i]
                output -= counts[i]
            else:
                return output - (k // i)
        
        return output
