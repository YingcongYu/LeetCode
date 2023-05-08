# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        ref = sorted(list(collections.Counter(arr).items()), key = lambda x: x[1])

        while ref:
            k -= ref[0][1]
            if k < 0:
                return len(ref)
            else:
                ref.pop(0)
        
        return len(ref)
