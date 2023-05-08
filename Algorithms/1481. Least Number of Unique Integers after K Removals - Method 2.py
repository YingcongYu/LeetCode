# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        ref = collections.Counter(arr)
        count = sorted(ref.values())
        output = len(ref)

        for i in count:
            if i == k:
                output -= 1
                break
            elif i > k:
                break
            else:
                k -= i
                output -= 1
        
        return output
