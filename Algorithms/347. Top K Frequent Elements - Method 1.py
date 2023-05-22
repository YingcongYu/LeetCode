# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ref = sorted(collections.Counter(nums).items(), key = lambda x: x[1], reverse = True)
        
        output = []
        for i in range(k):
            output.append(ref[i][0])
        
        return output
